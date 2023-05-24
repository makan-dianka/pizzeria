from django.shortcuts import render, redirect
from ..models.food import Food
from ..models.typefood import TypeFood

def food(request):

    pzrouge = Food.objects.filter(
        type=TypeFood.objects.get(food="pizza rouge"))

    pzblanche = Food.objects.filter(
        type=TypeFood.objects.get(food="pizza blanche"))
    
    pzcalzone = Food.objects.filter(
        type=TypeFood.objects.get(food="calzone"))
    
    boisson = Food.objects.filter(
        type=TypeFood.objects.get(food="boisson"))
    dessert = Food.objects.filter(
        type=TypeFood.objects.get(food="dessert"))

    context = {
        'pizza_calzone' : pzcalzone, 
        'pizza_rouge' : pzrouge, 
        'pizza_blanche' : pzblanche,
        'boisson' : boisson,
        'dessert' : dessert
        }
    
    # stockage des element du panier en session
    if request.method=="POST":
        id  = int(request.POST.get('id'))
        element = Food.objects.get(pk=id)
        try:
            request.session['total'] += element.prix
            request.session['selection'].append(
                {
                    'id': id, 'nom': element.nom,
                    'prix' : element.prix, 
                    'photo': element.photo.url, 
                    'desc' : element.desc, 
                    })
        except:
            request.session['total'] = element.prix
            request.session['selection'] = [{
                'id': id, 'nom': element.nom,
                'prix' : element.prix, 
                'photo': element.photo.url, 
                'desc' : element.desc,
                }]
        request.session.modified = True
    
        return redirect("/panier")

    return render(request, "pizzeria/pizza.html", context)