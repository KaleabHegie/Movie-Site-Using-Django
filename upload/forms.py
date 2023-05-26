from django import forms
from .models import *

class MoviesPost(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    year = forms.DateField(widget=forms.DateInput({
        'class' : 'form-control'
    }))
    resulution = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    duration = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    rating = forms.FloatField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    discription = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    genere = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    category = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    image = forms.FileField(widget=forms.FileInput({
        'class' : 'form-control'
    }))
    class Meta:
        model = Movie
        fields = '__all__'




class PricingPost(forms.ModelForm):
    type = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    montlyFee = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    vedioQuality = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    resulution = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    maxScreen = forms.IntegerField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    class Meta:
        model = Pricing
        fields = '__all__'  

        
class BlogPost(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    discription = forms.CharField(widget=forms.Textarea({
        'class' : 'form-control'
    }))
    image = forms.FileField(widget=forms.FileInput({
        'class' : 'form-control'
    }))
    class Meta:
        model = Blog
        fields = '__all__'


class contactPost(forms.ModelForm):
    adress = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    phone = forms.CharField(widget=forms.TextInput({
        'class' : 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput({
        'class' : 'form-control'
    }))
    class Meta:
        model = Contact
        fields = '__all__'            

           


