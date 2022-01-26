from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from blog_api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import hello.views

admin.autodiscover()
# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/
router = routers.DefaultRouter()
router.register('entries', views.EntryViewSet)
router.register('authors', views.AuthorViewSet)

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("grab/", include(router.urls)),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
]
