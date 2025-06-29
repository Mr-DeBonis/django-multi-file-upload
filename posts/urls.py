from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from posts import views

app_name = "posts"
urlpatterns = [
    path('', views.blog_view),
    path('<int:id>/', views.detail_view, name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)