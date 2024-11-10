from my_blog.models import My_blog
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class My_blogCreateView(CreateView):
    model = My_blog
    fields = ['title', 'content', 'preview']
    template_name = 'my_blogs/my_blog_form.html'
    success_url = reverse_lazy('my_blogs:blogs_list')


class My_blogListView(ListView):
    model = My_blog
    template_name = 'my_blogs/my_blogs_list.html'
    context_object_name = 'my_blogs'


class My_blogDetailView(DetailView):
    model = My_blog
    template_name = 'my_blogs/my_blogs_detail.html'
    context_object_name = 'my_blog'


class My_blogUpdateView(UpdateView):
    model = My_blog
    fields = ['title', 'content', 'preview']
    template_name = 'my_blogs/my_blogs_form.html'
    success_url = reverse_lazy('my_blogs:my_blogs_detail')


class My_blogDeleteView(DeleteView):
    model = My_blog
    template_name = 'my_blogs/my_blogs_confirm_delete.html'
    success_url = reverse_lazy('my_blogs:my_blogs_list')