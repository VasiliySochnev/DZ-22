from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from catalog.services import ProductService


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form_create.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    # def form_valid(self, form):
    #     product = form.save()
    #     user = self.request.user
    #     product.owner = user
    #     product.save()
    #     return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied

    # def get_success_url(self):
    #     return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = self.get_queryset()
        return context

    def get_queryset(self):
        queryset = cache.get("products_queryset")
        if not queryset:
            queryset = super().get_queryset()
            cache.set("products_queryset", queryset, 60 * 15)
        return queryset


@method_decorator(cache_page(60 * 15), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs["pk"]
        product = ProductService.get_product_by_id(product_id)
        context["product"] = product
        return context


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/categories.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = self.get_queryset()
        return context

    def get_queryset(self):

        catalogs = cache.get("catalogs")

        if catalogs is None:
            catalogs = Category.objects.all()
            cache.set("catalogs", catalogs, 60 * 15)

        return catalogs


class CategoryProductsListView(ListView):
    model = Product
    template_name = "catalog/category_product.html"
    context_object_name = "category_products_list"

    def get_queryset(self):

        category_id = self.kwargs.get("category_id")
        self.category = get_object_or_404(Category, pk=category_id)
        return ProductService.get_published_products_by_category(category_id)



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
