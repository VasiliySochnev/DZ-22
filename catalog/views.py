from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form_create.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_detail')

    # def get_success_url(self):
    #     return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')



class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


# def product_list(request):
#     products = Product.objects.all()
#     context = {'products': products}
#
#     return render(request, 'catalog/product_list.html', context)

# def contacts(request):
#     return render(request, 'catalog/contacts.html')


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



