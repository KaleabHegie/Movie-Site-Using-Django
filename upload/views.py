from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

# Normal template view
 
def homePage(request):
    context = {
        'upcoming': Movie.objects.filter(category = 'upcoming'),
        'toprated': Movie.objects.filter(category = 'toprated'),
        'worldBest': Movie.objects.filter(category = 'worldbest'),
    }
    return render(request , 'index.html' , context)
def moviePage(request):
    context = {
        'newReleased': Movie.objects.filter(category = 'newreleased'),
    }
    return render(request , 'movie.html' , context)
def tvShowPage(request):
    context = {
        'tvseries': Movie.objects.filter(category = 'tvseries')
    }
    return render(request , 'tv-show.html' , context)
def pricingPage(request):
    context = {
        'pricing': Pricing.objects.all()
    }
    return render(request , 'pricing.html' , context)
def blogPage(request):
   
    recentblog = []
    j = 0
    for i in Blog.objects.all():
        recentblog.append(i)
        j = j+1 
        if j >= 2:
            break 

    context = {
        'blog': Blog.objects.all(),
        'recentblog': recentblog
    }

    return render(request , 'blog.html' , context)
def contactPage(request):
    context = {
        'contact': Contact.objects.all(),
    }
    return render(request , 'contact.html' , context)

def movieDetailPage(request , pk):
    context = {
        'movie': Movie.objects.get(id = pk),
    }
    return render(request , 'movie-details.html' , context)



# Form VIews


def createBlogPost(request):
    form = BlogPost(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = BlogPost()
    context = {
        'form':form
    }
    return render(request, 'forms/BlogPostform.html', context)

def createPricingPost(request):
    form = PricingPost(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = PricingPost()
    context = {
        'form':form
    }
    return render(request, 'forms/PricingPostform.html', context)

def createMoviesPost(request):
    form = MoviesPost(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = MoviesPost()
    context = {
        'form':form
    }
    return render(request, 'forms/MoviesPostform.html', context)

def changeContact(request):
    form = contactPost(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = contactPost()
    context = {
        'form':form
    }
    return render(request, 'forms/ChangeContact.html', context)
