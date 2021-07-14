
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.models import User


class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body', 'executor']
    template_name = 'post_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.executor = self.request.user
        return super(BlogCreateView, self).form_valid(form)

    def get_readonly_fields(self, request, obj=None):
        if not self.request.user.is_superuser:
            return ['executor']
        else:
            return []


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home')
