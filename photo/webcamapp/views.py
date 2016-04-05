from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from webcamapp.models import Photo
# Create your views here.


class WebcamPhoto(CreateView):
    model = Photo
    fields = ['camera',]
    template_name = 'webcamapp/camera.html'
    success_url = reverse_lazy('camera')

    def get_context_data(self, *args, **kwargs):
        context=super(WebcamPhoto, self).get_context_data(*args, **kwargs)
        context['cameras']=Photo.objects.all()
        return context
