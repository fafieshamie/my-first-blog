from django.shortcuts import render
from django.utils import timezone
from .models import Post
from.forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404


def fileView(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return	render(request,'blog/post_list.html', {'posts': posts})

def post1(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return	render(request,'blog/post1.html', {'posts': posts})
  
def post2(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return	render(request,'blog/post2.html', {'posts': posts})
    
def post3(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return	render(request,'blog/post3.html', {'posts': posts})
    
def post_detail(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return	render(request,'blog/post_detail.html', {'posts': posts})
    

    
def	post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',	{'post': post})
 
def	post_new(request):				
    form = PostForm(request.POST)
    return	render(request, 'blog/post_edit.html', {'form': form})
    if	request.method == "POST":
        [...] 
    else:				
        form = PostForm()
        
    if	form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail',pk=post.pk)
    
def	post_new(request, pk):
    post= get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author	= request.user
            post.published_date	= timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return	render(request, 'blog/post_edit.html',{'form':form})
    
def	post_edit(request,	pk):				
    post = get_object_or_404(Post,	pk=pk)				
    if	request.method == "POST":								
        form = PostForm(request.POST, instance=post)
        if	form.is_valid():												
            post = form.save(commit=False)												
            post.author = request.user												
            post.published_date = timezone.now()												
            post.save()												
            return redirect('post_detail', pk=post.pk)				
    else:								
        form = PostForm(instance=post)				
        return render(request, 'blog/post_edit.html', {'form':	form})
        
def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'post' : posts})

