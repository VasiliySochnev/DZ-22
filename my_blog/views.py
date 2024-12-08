from my_blog.models import My_blog
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class My_blogCreateView(CreateView):
    model = My_blog
    fields = ["title", "content", "preview", "publication_sign"]
    template_name = "my_blogs/my_blog_form.html"
    success_url = reverse_lazy("my_blog:my_blogs_list")


class My_blogListView(ListView):
    model = My_blog
    template_name = "my_blogs/my_blogs_list.html"
    context_object_name = "my_blogs"

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset


class My_blogDetailView(DetailView):
    model = My_blog
    template_name = "my_blogs/my_blogs_detail.html"
    context_object_name = "my_blog"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class My_blogUpdateView(UpdateView):
    model = My_blog
    fields = ["title", "content", "preview", "publication_sign"]
    template_name = "my_blogs/my_blog_form.html"

    def get_success_url(self):
        return reverse("my_blog:my_blogs_detail", args=[self.kwargs.get("pk")])


class My_blogDeleteView(DeleteView):
    model = My_blog
    template_name = "my_blogs/my_blogs_confirm_delete.html"
    success_url = reverse_lazy("my_blog:my_blogs_list")
