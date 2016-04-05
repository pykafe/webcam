from __future__ import unicode_literals

from django.db import models
from webcam.fields import CameraField

# Create your models here.

class Photo(models.Model):

    camera = CameraField('Please upload Photo', format='png', blank=True, null=True, upload_to='images')
