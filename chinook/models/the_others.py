from django.db import models




# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class MediaType(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Genre(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    media_types = models.ManyToManyField(MediaType, through='Album', related_name='genres')
    





class Album(models.Model):
    title = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='albums', null=True)
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE, related_name='albums', null=True)
    def __str__(self):
        return self.title

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='albums')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres')
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE, related_name='tracks')
    name = models.CharField(max_length=255, null=False)
    composer = models.CharField(max_length=255, null=True)
    milliseconds = models.IntegerField(null=False)
    bytes = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Playlist(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tracks = models.ManyToManyField(Track, related_name="playlists")