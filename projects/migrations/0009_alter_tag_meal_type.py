# Generated by Django 3.2.7 on 2021-12-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_food_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='meal_type',
            field=models.CharField(choices=[('bf', 'Breakfast'), ('ln', 'Launch'), ('dn', 'Dinner')], default='', max_length=10),
        ),
    ]