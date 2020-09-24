from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    # to get a limited set of objects
    #blogs = Blog.objects.order_by('-date')[:5]
    blogs = Blog.objects.order_by('-date')
    return render(request,'blog/all_blogs.html',{'blogs' : blogs})

def detail(request,blog_id):
    # to get the page if page not found then throw 404 error
    # get_object_or_404(name_of_cls,pk = primary key)
    blog = get_object_or_404(Blog, pk= blog_id)
    return render(request,'blog/detail.html',{'blog' : blog})
