from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime

class Playlist(models.Model):
    name = models.CharField(max_length=200)
    albums = models.ManyToManyField('Album')
    publish = models.BooleanField()
    publish_accepted = models.BooleanField()
    created_by = models.ForeignKey(
                                    settings.AUTH_USER_MODEL,
                                    related_name="playlists",
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(
                                    settings.AUTH_USER_MODEL,
                                    related_name="bands",
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Album(models.Model):

    UNKNOWN = 'UN'
    NEW = 'NE'
    LIKE_NEW = 'LN'
    VERY_GOOD = 'VG'
    GOOD = 'GO'
    ACCEPTABLE = 'AC'
    BAD = 'BA'

    STATE_CONDITION_CHOICES = (
        (UNKNOWN, 'Unknown'),
        (NEW, 'New'),
        (LIKE_NEW, 'Like New'),
        (VERY_GOOD, 'Very Good'),
        (GOOD, 'Good'),
        (ACCEPTABLE, 'Acceptable'),
        (BAD, 'Bad'),
    )

    band_name = models.ForeignKey('Band', related_name="albums", on_delete=models.CASCADE)
    album_name = models.CharField(max_length=200)
    published_year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1800, message='This album is not THAT old!'), MaxValueValidator(datetime.today().year, message="You can't buy albums from the future")])
    edition_year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1800, message='This album is not THAT old!'), MaxValueValidator(datetime.today().year, message="You can't buy albums from the future")])
    bought_year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1800, message='This album is not THAT old!'), MaxValueValidator(datetime.today().year, message="You can't buy albums from the future")])
    price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0, message='You cannot pay negative money...'), MaxValueValidator(10000, message="No. Just no.")])
    country = models.CharField(blank=True, null=True, max_length=50)
    state_condition = models.CharField(
                                        max_length=2,
                                        choices=STATE_CONDITION_CHOICES,
                                        default=UNKNOWN)
    observations = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
                                settings.AUTH_USER_MODEL,
                                related_name="albums",
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.band_name} - {self.album_name}'
