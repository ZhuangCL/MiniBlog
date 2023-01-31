from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20, help_text='Enter a article genre (e.g. Gossip, Movie Function)') 

    def __str__(self):
        return self.name
#_______________________________________________________

class Blogger(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True)

    SEX_CHOICE = (
        (0, 'Female'),
        (1, 'Male'),
    )
    sex = models.IntegerField(choices=SEX_CHOICE,default=1)
    
    date_of_birth= models.DateField(null=True, blank=True)


    class Meta:
        ordering = ['user']
        permissions = (("can_edit_all_SET", "can edit all"),)
        permissions = (("can_create_articles", "can write articles"),)

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])
    def __str__(self):
        return self.user.username
#_______________________________________________________

from django.urls import reverse
class Article(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this article')
    content = models.TextField(max_length=3000, help_text='Enter content of the article')
    issusing_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['issusing_time']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
#_______________________________________________________

class ArticleInstance(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(max_length=300, help_text='Enter comment of the article')
    post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post_time']

    def __str__(self):
        len_title=50
        if len(self.comment)>len_title:
            titlestring=self.comment[:len_title] + '...'
        else:
            titlestring=self.comment
        return titlestring
