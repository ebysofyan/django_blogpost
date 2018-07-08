from django.shortcuts import render
from django.views import View
from .models import Category, Post
# Create your views here.


class PostsListView(View):
    template_name = 'post_list.html'

    def get(self, request):
        cat = request.GET.get('category', None)

        if cat:
            posts = Post.objects.filter(category__name=cat)
        else:
            posts = Post.objects.all()

        context_data = {
            'categories': Category.objects.all(),
            'posts': posts
        }
        return render(request, self.template_name, context_data)


class PostsDetailView(View):
    template_name = 'post_detail.html'

    def get(self, request, slug):
        context_data = {
            'categories': Category.objects.all(),
            'post': Post.objects.get(slug=slug)
        }
        return render(request, self.template_name, context_data)
