from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import food
from .models import Tag
from .models import Reservation
from .utils import Search
from .utils import search_food
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
def search(request):
    foods = food.objects.all()
    if request.method == "GET":
        search = request.GET.get('search')
        print(">>>>>>>>>>>>>>>>>>>>>>>>>")
        result = food.objects.distinct().filter(
        Q(item__icontains=search) | Q(description__icontains = search)|Q(tags__meal_type__icontains=search))
        context = {
            'result':result,}
        return render(request,'search.html',context)
    else:
        return render(request,'#')
def tags(request):
    bf,ln,din,des,dri =  Search(request)
    all_projects = food.objects.all()
   
    context = {'a': all_projects,
                'bf': bf,
                'ln': ln,
                'din': din,
                'des': des,
                'dri': dri,
                
                }
    return context


def home(request):

    context = tags(request)
    
    return render(request,'home.html',context)
def home_page(request): 
    context = tags(request)
    return render(request,'home.html',context)





def single_page(request,food_id):
    project = food.objects.get(id=food_id)
    context = {'project': project}
    return render(request, 'shop-single.html', context)

def menu_page(request):
    context = tags(request)
    return render(request,'menu.html',context)
    
def about(request):
    return render(request,'about.html')

# def search(request):
# 	if request.method == "POST":
# 		searched = request.POST['searched']
# 		x = food.objects.filter(item__contains=searched)
	
# 		return render(request, 
# 		'home/search.html', 
# 		{'searched':searched,
# 		'x':x})
        

def reservation(request):
    if request.POST.get("people"):
        people = request.POST.get("people")
        email = request.POST.get("email")
        date = request.POST.get("date")
        time = request.POST.get("time")
        print(people)
        aaa = Reservation(people= people,email=email,date=date,time=time)
        aaa.save()
        subject , from_email, to = 'About the reservation at----', 'supply171837@gmail.com',email
        text_content = '''Thank you for your reservation. The confirmation is pending! We will text you soon!'''
       
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        # msg.attach_alternative(html_content, "")
        msg.send()
        return redirect('reservation')
    
    return render(request,'reservation.html')
   
