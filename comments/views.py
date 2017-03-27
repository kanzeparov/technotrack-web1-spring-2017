from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Comment
from posts.models import Post
from django.views.generic import DetailView, ListView, UpdateView, CreateView

class CommentView(DetailView, CreateView):
    queryset = Post.objects.all()
    model = Comment
    template_name = 'comments/comment.html'
    fields = ('title', 'description')
    success_url = '/blogs/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CommentView, self).form_valid(form)

