from django.shortcuts import render

def panier(request):
    context = {}
    if request.method=="POST":
        id = int(request.POST.get('id'))
        try:
            s = request.session['selection']
            for items in s:
                if id == items['id']:
                    request.session['selection'].remove(items)
                    request.session.modified = True

                    total = request.session['total'] - items['prix']

                    request.session['total'] = total
                    request.session.modified = True 
        except:
            pass

    if 'selection' in request.session:
        context['session'] = len(request.session['selection'])

    return render(request, "pizzeria/panier.html", context)
