from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=255)
    album_title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=255)
    song_title = models.CharField(max_length=255)
    song_url = models.CharField(default='https://musicpleer.bz/#!98f3c34ee7b892a91c370cb124229dac', max_length=1000)

    def __str__(self):
        return self.song_title

    class Meta:
        verbose_name_plural = "Songs"
