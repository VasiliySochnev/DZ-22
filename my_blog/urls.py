from django.urls import path
from my_blog import views
from my_blog.apps import MyBlogConfig
from config import settings
from django.conf.urls.static import static

app_name = MyBlogConfig.name

urlpatterns = [
    path("my_blogs_list/", views.My_blogListView.as_view(), name="my_blogs_list"),
    path(
        "my_blogs_detail/<int:pk>/",
        views.My_blogDetailView.as_view(),
        name="my_blogs_detail",
    ),
    path(
        "my_blog_form/<int:pk>/", views.My_blogCreateView.as_view(), name="my_blog_form"
    ),
    path(
        "my_blog_update/<int:pk>/",
        views.My_blogUpdateView.as_view(),
        name="my_blog_update",
    ),
    path(
        "my_blogs_confirm_delete/<int:pk>/",
        views.My_blogDeleteView.as_view(),
        name="my_blog_delete",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
