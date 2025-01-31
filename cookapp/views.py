from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import BlogPost
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, TemplateView
from .forms import BlogPostForm
from django.urls import reverse_lazy
from django.db.models import Q
from taggit.models import Tag



class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'orderby_records'
    queryset = BlogPost.objects.order_by('-posted_at')
    paginate_by = 4

class BlogDetail(DetailView):
    template_name='post.html'
    model = BlogPost

class BlogPostCreateView(CreateView):
    form_class = BlogPostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('cookapp:post_success')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class BlogPostSuccessView(TemplateView):
    template_name = 'post_success.html'

class PostListView(ListView):
    model = BlogPost
    template_name = 'post_list.html'
    context_object_name = 'orderby_records'
    paginate_by = 10

class SearchResultsView(ListView):
    model = BlogPost
    template_name = 'search.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            tag_ids = Tag.objects.filter(name__icontains=query).values_list('id', flat=True)
            return BlogPost.objects.filter(
                Q(title__icontains=query) | 
                Q(material__icontains=query) | 
                Q(content__icontains=query) | 
                Q(tags__in=tag_ids)
            ).distinct()
        return BlogPost.objects.none()
    
class UserView(ListView):
    template_name = "post_list.html"
    paginate_by = 9

    def get_queryset(self):
        user_id = self.kwargs["user"]
        user_list = BlogPost.objects.filter(user=user_id).order_by("posted_at")
        return user_list
    
class PostListView(ListView):
    model = BlogPost
    template_name = 'post_list.html'
    context_object_name = 'orderby_records'
    paginate_by = 10

    def get_queryset(self):
        user_id = self.request.GET.get('user')
        if user_id:
            return BlogPost.objects.filter(user=user_id).order_by('-posted_at')
        return BlogPost.objects.order_by('-posted_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.GET.get('user')
        if user_id:
            context['username'] = BlogPost.objects.filter(user=user_id).first().user.username
        return context