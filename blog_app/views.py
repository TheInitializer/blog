import datetime
from django.shortcuts import get_object_or_404, render
from .models import Post, Comment
from .forms import CommentForm
import markdown2

# Create your views here.
def post(request, slug):
	p = get_object_or_404(Post, slug=slug)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			new_comment = Comment.objects.create(
				time=datetime.datetime.now(),
				name=cd['name'],
				content=cd['content'],
				post=p)
	else:
		form = CommentForm()
	comments = Comment.objects.filter(post=p)
	print(comments)
	context = {
		'title': p.title, 
		'date': p.date, 
		'content': markdown2.markdown(p.content),
		'comments': comments,
		'comment_form': form}
	return render(request, 'post.html', context)

def home(request):
	posts = Post.objects.all()
	context = {'posts': posts}
	return render(request, 'home.html', context)
