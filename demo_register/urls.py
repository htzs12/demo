
from django.urls import path,include,re_path

from . import views

app_name = 'demo_register'

urlpatterns = [
    path('',views.RegisterView.as_view(),name='register'),
    path('image/',views.RegisterView.as_view(),name='image'),
    path('image_demo/',views.image_demo,name='image_demo'),
    path('modify/',views.modifyView.as_view(),name='modify'),
    path('del_demo/',views.del_demo,name='del_demo'),
]