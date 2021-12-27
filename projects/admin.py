from django.contrib import admin
from .models import food,Tag


class Food(admin.ModelAdmin):
   
   list_display = ('item','Tags','id',)
   def Tags(self, obj):
        return ", ".join([t.meal_type for t in obj.tags.all()])

class FoodTag(admin.ModelAdmin):
    pass
admin.site.register(food,Food)
admin.site.register(Tag,FoodTag)