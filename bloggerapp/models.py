from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Category(models.Model):
    title= models.CharField(max_length= 255)
    slug= models.SlugField()


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    category=models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE )
    title= models.CharField(max_length=255)
    intro= models.TextField()
    body= models.TextField()
    slug= models.SlugField()
    date_added= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    post= models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    body= models.TextField()
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)