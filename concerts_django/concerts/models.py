from django.db import models

# Create your models here.

class Concert(models.Model):
    # PK id created by default id (bigint), you may override that with th e
    # following line
    # id = models.SmallIntegerField(auto_increment=True, primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField()
    venue = models.CharField(max_length=200, unique=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
    		return self.name

class Song(models.Model):
    title = models.CharField(max_length=200, unique=True)
    duration = models.TimeField()
    genre = models.CharField(max_length=50, unique=True)

class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True)
    concerts = models.ManyToManyField(Concert)
    songs = models.ManyToManyField(Song)
    class Meta:
        ordering = ['name']