from django.db import models

# Create your models here.
class Post(models.Model):
	date = models.DateField('Date published')
	slug = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=5000)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['date']

class Comment(models.Model):
	time = models.DateTimeField('Time submitted')
	name = models.CharField(max_length=100)
	content = models.TextField(max_length=1000)
	post = models.ForeignKey(Post)
