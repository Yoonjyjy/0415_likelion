from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post2
from .forms import PostForm

# Create your views here.
def selfhome(request) :
    posts = Post2.objects
    return render (request, 'selfintro/selfhome.html', {'posts':posts})

def selfdetail(request, post_id) :
    post_detail = get_object_or_404(Post2, pk=post_id)
    return render(request, 'selfintro/selfdetail.html', {'posts':post_detail})

def post_new2(request) :
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect('selfdetail', post_id=post.pk)
    else :
        form = PostForm()
        return render(request, 'selfintro/new2.html', {'form':form})