from django.shortcuts import render

# Create your views here.
from restauracja_app.models import Restauracja, Type


def add_restaurant(request):
    if request.method == 'GET':
        return render(request, 'add_restaurant.html')
    else:
        name = request.POST.get('name')
        address = request.POST.get('address')
        Restauracja.objects.create(name=name, address=address)
        return render(request, 'add_restaurant.html')


def show_all(request):
    list = Restauracja.objects.all()
    context = {'list': list}
    return render(request, "restaurants.html", context)


def show_info(request, id):
    element = Restauracja.objects.get(id=id)
    return render(request, 'restauracja_info.html', {'nazwa': element.name, 'adres': element.address})


def add_types(request):
    if request.method == 'GET':
        return render(request, 'add_type.html')
    else:
        name = request.POST.get('name')
        Type.objects.create(name=name)
        return render(request, 'add_type.html', {'info': 'Dodano nowy typ'})
def show_types(request):
    list = Type.objects.all()
    context = {'list': list}
    return render(request, "types.html", context)


