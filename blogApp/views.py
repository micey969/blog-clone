from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404,redirect
from blogApp.forms import PostForm,CommentForm
from blogApp.models import Post,Comment
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView,
                                CreateView, UpdateView,DeleteView)

# Create your views here.
class AboutView(TemplateView):
    template_name = 'blogApp/about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self): 
        query = self.request.GET.get("search")

        if query:
            object_list = Post.objects.filter((Q(text__icontains=query) | Q(title__icontains=query)) & Q(date_published__lte=timezone.now()))
        else:
            object_list = Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')
        
        return object_list


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date_published__isnull=True).order_by('date_created')


####

@login_required
def post_published(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blogApp/comment_form.html',{'form':form})


@login_required
def comment_approved(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk )