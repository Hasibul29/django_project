from django.contrib import admin
from .models import food,Tag,Reservation


class Food(admin.ModelAdmin):
   
   list_display = ('item','Tags','id',)
   def Tags(self, obj):
        return ", ".join([t.meal_type for t in obj.tags.all()])

class FoodTag(admin.ModelAdmin):
    pass


class Reservations(admin.ModelAdmin):
    # fields = ('title', 'tags', 'created')
    search_fields = ['status']
    list_editable = ['status']
    list_display = ('people', 'date', 'time',
                    'status')

    
admin.site.register(food,Food)
admin.site.register(Tag,FoodTag)
admin.site.register(Reservation,Reservations)