from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.say_hello),
    path('hi/', views.hi),
    path('productlist/', views.productList),
    path('fieldquerying/', views.relatedField),
    path('orderedItem/', views.orderItem),
    path('fields/', views.fields),
    path('related/', views.relatedField),
    path('calculation/', views.aggregate),
    path('annotation/', views.annotation),
    path('func/', views.func),
    path('group/', views.grouping)
]