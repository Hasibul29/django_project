from django.db import models
import uuid

class Tag(models.Model):
    Breakfast = 'Breakfast'
    Lunch = 'Lunch'
    Dinner = 'Dinner'
    Dessert = 'Dessert'
    Drinks = 'Drinks'
    food = [(Breakfast, 'Breakfast'),
        (Lunch, 'Lunch'),
        (Dinner, 'Dinner'),
        (Dessert,'Dessert'),
        (Drinks,'Drinks'),]
    meal_type = models.CharField(max_length= 10, choices=food,null=True,blank=True,unique=True)
    id = models.UUIDField(default=uuid.uuid4,null=False,
                         primary_key=True,editable=False)
    def __str__(self)->str:
        return  str(self.meal_type)
class food(models.Model):

    item = models.CharField(max_length=200)
    price = models.IntegerField(null=True,blank=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='static/assets/images/menu/dish',null=True)
    description = models.TextField(max_length=1000)
    id = models.UUIDField(default=uuid.uuid4,null=False,
                         primary_key=True,editable=False)

    def __str__(self)->str:
        return str(self.item)

class Reservation(models.Model):
    Pending = 'Pending'
    Accepted = 'Accepted'
    Rejected = 'Rejected'
    status = [(Pending, 'Pending'),
        (Accepted, 'Accepted'),
        (Rejected, 'Rejected'),
        ]
    people = models.CharField(max_length=20)
    date = models.DateField()
    email =models.CharField(max_length=50)
    time = models.TimeField()
    status = models.CharField(max_length=10,choices=status,default='Pending')

    
