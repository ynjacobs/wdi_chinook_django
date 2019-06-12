from django.db import models



class Album(models.Model):
    title = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='albums')
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE, related_name='albums')
    def __str__(self):
        return self.title