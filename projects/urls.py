from . import views
# from .models import food
from django.urls import path


urlpatterns = [
    path('', views.home),
    path('home/', views.home_page,name="home"),
    path('menu/', views.menu_page,name="menu"),
    path('menu/shop-single/<str:food_id>/', views.single_page,name="menu_page"),
    path('search',views.search,name='search'),
    path('reservation',views.reservation,name='reservation'),
    path('about/', views.about,name="about"),
    
]

