from django.db import models
from webcam.fields import CameraField

# Create your models here.

class PhotoPerson(models.Model):

    picture = CameraField('Please upload Photo', format='jpeg', blank=True, null=True, upload_to='images')

    def __str__(self):
        return ' %s' % self.picture
