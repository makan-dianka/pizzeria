from django.shortcuts import render, redirect
from .. models.commande import Commande
from .. models.order import OrderFood
from ..models.food import Food
from boulange import settings
import stripe 
from . import func


def paiement(request):
    context = {}
    if request.method=="POST":

        stripe.api_key = settings.STRIPE_TEST_KEY
        stripeToken = request.POST.get('stripeToken')

        # Create customer 
        customer = stripe.Customer.create(
                name=request.POST.get("name"),
                email=request.POST.get('email'),
                source=stripeToken,
            )

        amount = int(request.session['total'])

        try:
            # Charge card 
            stripe.Charge.create(
                customer=customer,
                amount=amount*100,
                currency='eur',
                description="Pizzeria Boul.ange"
            )
        except Exception as e:
            context['card_error'] = e
        else:
            # enregistrement de la commande 
            token = func.gentoken()
            commande = Commande()
            name = request.POST.get('name')
            email = request.POST.get('email')

            commande.username = name
            commande.useremail = email
            commande.commentaire = request.POST.get('commentaire')
            commande.carte = stripeToken
            commande.number = token
            commande.save()

            func.qrcode(request, token)
            func.genpdf(request, amount, token)
            # func.sendmail(request, name, email)

            ids = [product['id'] for product in request.session['selection']]
            check = []

            # enregistrement des order_food 
            for id in ids:
                if id not in check:
                    command = OrderFood()
                    command.quantite = ids.count(id)
                    command.food = Food.objects.get(pk=id)
                    command.save()
                    commande.fk_orderfood.add(command)
                check.append(id)

            # destruction de session après la commande 
            del request.session['selection']
            request.session.modified = True 
            del request.session['total']
            request.session.modified = True

            return redirect("/success")
    return render(request, 'pizzeria/paiement.html', context)
