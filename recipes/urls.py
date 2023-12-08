from django.urls import path
from recipes.views import home, sobre, contato

# HTTP REQUEST <- HTTP RESPONSE
# HTTP REQUEST


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
