from django.urls import path
from recipes import views

# HTTP REQUEST <- HTTP RESPONSE
# HTTP REQUEST


app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipes, name="recipe"),
]
