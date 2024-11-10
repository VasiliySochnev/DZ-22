from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


# def product_list(request):
#     products = Product.objects.all()
#     context = {'products': products}
#
#     return render(request, 'catalog/product_list.html', context)

# def contacts(request):
#     return render(request, 'catalog/contacts.html')

class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

# def product_info(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#
#     return render(request, 'catalog/product_info.html', context)

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         return HttpResponse(f'Спасибо, {name}! Сообщение получено.')
#     return render(request, "contacts.html")
#



