from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homePage, name='Home'),
    path('movie/',views.moviePage, name='Movie'),
    path('tvshows/',views.tvShowPage, name='TvShow'),
    path('movie/<str:pk>/',views.movieDetailPage, name='MovieDetail'),
    path('pricing/',views.pricingPage, name='Pricing'),
    path('blog/',views.blogPage, name='Blog'),
    path('contact/',views.contactPage, name='Contact'),

    #form paths
    path('form/', views.createMoviesPost , name='createMoviesPost'),
    path('BlogPostform/', views.createBlogPost , name='createBlogPost'),
    path('PricingPostform/', views.createPricingPost , name='createPricingPost'),
    path('ChangeContactform/', views.changeContact , name='changeContact'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)