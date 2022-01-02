from .models import food, Tag
from django.db.models import Q


def Search(request):
    bf = food.objects.filter(tags__meal_type='Breakfast')
    ln = food.objects.filter(tags__meal_type='Lunch')
    din =food.objects.filter(tags__meal_type='Dinner')
    des =food.objects.filter(tags__meal_type='Dessert')
    dri =food.objects.filter(tags__meal_type='Drinks')
    sp =food.objects.filter(tags__meal_type='Special')
    return bf,ln,din,des,dri,sp

def search_food(request):

    search_query = ''

    if request.GET.get('search'):
        search_query = request.GET.get('search')

    tags = Tag.objects.filter(meal_type=search_query)

    projects = food.objects.distinct().filter(
        Q(item__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(tags__in=tags)
       
    )
    return projects, search_query