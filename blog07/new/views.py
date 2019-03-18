from django.shortcuts import render

# Create your views here.

from new.models import Post  

posts=[{

}]

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'new/home.html',context)

def about(request):

    return render(request,'new/about.html')

def content(request):

    return render(request,'new/content.html')