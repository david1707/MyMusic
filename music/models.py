from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

class Band(models.Model):
    band_name = models.CharField(max_length=200)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.band_name


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

    band_name = models.ForeignKey('Band', on_delete=models.CASCADE)
    album_name = models.CharField(max_length=200)
    bought_year = models.IntegerField(blank=True, null=True)
    edition_year = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    country = models.CharField(blank=True, null=True, max_length=50)
    state_condition = models.CharField(max_length=2, choices=STATE_CONDITION_CHOICES, default=UNKNOWN)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.band_name} - {self.album_name}'