from django.shortcuts import render, resolve_url
from django.views.generic import DetailView, ListView
from .models import Comment
from posts.models import Post
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy


class CommentView(DetailView, CreateView):
    queryset = Post.objects.all()
    model = Comment
    template_name = 'comments/comment.html'
    fields = ('text',)
    postob = None
    pk = 0
    # success_url = '/blogs/'
    def get_success_url(self):
        return resolve_url('blogs:postview', pk=self.postob.pk)
    # def get_form(self, form_class=None):
    #     form = super(CommentView, self).get_form()
    #     return form


    def dispatch(self, request, *args, **kwargs):
        self.postob = get_object_or_404(Post, id=kwargs['pk'])
        return super(CommentView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CommentView, self).get_context_data(**kwargs)
        context['post'] = self.postob
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.postob
        return super(CommentView, self).form_valid(form)

