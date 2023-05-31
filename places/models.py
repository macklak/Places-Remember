
from django.db import models
from allauth.socialaccount.models import SocialAccount

class memories(models.Model):
    name = models.CharField(max_length=100)
    comment =models.TextField(blank=True)
    mapPlaceWeiht=models.FloatField()
    mapPlaceLongitude = models.FloatField()
    useruid=models.ForeignKey(SocialAccount ,on_delete=models.CASCADE)

