from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="shophome"),
    path("about/",views.about,name="aboutshop"),
    path("contact/",views.contact,name="contactshop"),
    path("tracker/",views.tracker,name="trackershop"),
    path("search/",views.search,name="searchshop"),
    path("productview /",views.productview,name="productviewshop"),
    path("checkout/",views.search,name="checkoutshop"),
 #   path("search/",views.search,name="searchshop"),
  #   path("search/",views.search,name="searchshop"),

]
