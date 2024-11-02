from django.shortcuts import render, get_object_or_404
from catalog.models import Product

from django.http import HttpResponse


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)

# def home(request):
#     return render(request, 'catalog/home.html')
#
def contacts(request):
    return render(request, 'catalog/contacts.html')

def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product,
               }

    return render(request, 'catalog/product_info.html', context)

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         return HttpResponse(f'Спасибо, {name}! Сообщение получено.')
#     return render(request, "contacts.html")
#
# def home(request):
#     if request.method == 'GET':
#         return render(request, 'home.html')


