from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from FoodFunda import settings
from FoodFunda.settings import *
from recipe import views

urlpatterns = [
    path('',views.index,name='index'),
    path('upload/',views.upload,name='upload-recipe'),
    path('update/<int:recipe_id>',views.update,name='update_recipe'),
    path('delete/<int:recipe_id>',views.delete,name='delete_recipe'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)