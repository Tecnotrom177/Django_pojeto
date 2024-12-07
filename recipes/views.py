from django.shortcuts import render, get_list_or_404, get_object_or_404
from ultils.recipes.factory import make_recipe
from django.http import Http404
from recipes.models import Recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
    
def category(request, category_id):
    #recipes = Recipe.objects.filter(category__id = category_id, is_published=True).order_by('-id')
    
    #Uma maneira de resolver o problema da pagina não encontrada
    #category_name = getattr(
    #    getattr(recipes.first(), 'category', None), 'name', 'Not Found'
    #)
    
    #if not recipes:
        #return HttpResponse(content='Not Foud', status=404)
        #raise Http404('Not Found')
    
    recipes = get_list_or_404(Recipe.objects.filter(category__id = category_id, is_published=True).order_by('-id'))
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category -'   
    })
    
def recipe(request, recipe_id):
    recipes = Recipe.objects.filter(id = recipe_id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipes': recipes,
        'is_detail_page': True,
    })