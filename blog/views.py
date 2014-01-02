from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class PublishedPostsMixin(object):
    def get_queryset(self):
        """
        queryset = super(PublishedPostsMixin, self).get_queryset()
        return queryset.filter(published=True)
        """
        return self.model.objects.live()

class PostListView(PublishedPostsMixin, ListView):
    model = Post    

class PostDetailView(PublishedPostsMixin, DetailView):
    model = Post

        
        
"""
function bases views are done like this:)

from django.shortcuts import render

def blog_list(request, *args, **kwargs):
    post_list = Post.objects.filter(published=True)
    template_name = "post_list.html"

    context = {
        "post_list": post_list
    }
    
    return render(request, template_name, context)

def blog_detail(request, pk, *args, **kwargs):
    post = Post.objects.get(pk=pk, published=True)
    template_name = "blog/post_detail.html"

    context = {
        "post": post
    }

    return render(request, template_name, context) 
    
"""           