from django.shortcuts import render

# Create your views here.


def showHome(request):
    return render(request, 'page/index.html')

def showAnimals(request):
    return render(request, 'page/animal.html')

def showProductos(request):
    return render(request,"page/producto.html")
