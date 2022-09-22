from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    title = models.CharField(max_length=256)
    # text = models.TextField()
    text = RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now())
    date_published = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

# has to be called this method
# eventually we will make a post_detail view
# this creates an absolute link for each blog post and takes you to that specific post
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blogApp.Post',related_name='comments', on_delete= models.CASCADE)
    author = models.CharField(max_length=200)
    text = RichTextField(blank=True, null=True)
    # text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

# after entering a comment, the user is taken back to the home page 
# which lists all the blog posts
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text