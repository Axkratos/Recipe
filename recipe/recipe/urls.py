from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from vege.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", receipes, name='receipes'),
    path("delete_receipe/<id>", delete_receipe, name='delete_receipes'), 
    path("update_receipe/<id>", update_receipe, name='update_receipes'),
    path("receipes", upload_receipes, name='upload_receipes'),
    path("login", login_page, name='login'),
    path("register", register_page, name='register'),
    path("logout", logout_page, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  