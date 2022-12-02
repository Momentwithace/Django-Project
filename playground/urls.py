from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.say_hello),
    path('hi/', views.hi),
    path('productlist/', views.productList),
    path('fieldquerying/', views.relatedField)
]