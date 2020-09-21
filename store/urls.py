#from .views import index
from . import views
from django.urls import path, include
urlpatterns = [
        path('' , views.index),
        path('index' , views.index),
        path('shop' , views.shop),
        path('cart' , views.cart),
        path('about' , views.about)

]
