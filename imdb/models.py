from django.db import models

# Create your models here.

class Actor(models.Model):
    actor_id =models.CharField(max_length=200,primary_key = True)
    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)
    fb_likes=models.CharField(max_length=100)

class Director(models.Model):
    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)
    no_of_facebook_likes = models.CharField(max_length=100)
    

class Movie(models.Model):
    movie_id = models.CharField(max_length = 200,primary_key = True)
    name = models.CharField(max_length=100)
    collections = models.FloatField()
    year_of_release = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    avg_rate = models.CharField(max_length=100)
    imdb_link = models.URLField()
    budget = models.CharField(max_length=100)
    image = models.URLField(null = True)
    genere =  models.CharField(max_length = 100)
    duration = models.CharField(max_length=100)
    no_of_users_voted = models.CharField(max_length=100)
    director = models.ForeignKey(Director,on_delete = models.CASCADE)
    actors = models.ManyToManyField(Actor,through='Cast')

class Cast(models.Model):
    role = models.CharField(max_length = 50)
    actor=models.ForeignKey(Actor,on_delete = models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete = models.CASCADE)
    pay_actor = models.FloatField(default=0)
    pay_direct = models.FloatField(default=0)
   








