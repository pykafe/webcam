from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from webcamapp.models import PhotoPerson
# Create your views here.


class WebcamPhoto(CreateView):
    model = PhotoPerson
    fields = ['picture',]
    template_name = 'webcamapp/camera.html'
    success_url = reverse_lazy('camera')

    def get_context_data(self, *args, **kwargs):
        context = super(WebcamPhoto, self).get_context_data(*args, **kwargs)
        context['cameras']=PhotoPerson.objects.all()
        return context


class PhotoUpdate(UpdateView):
    model = PhotoPerson
    fields = ['picture',]
    template_name = 'webcamapp/camera.html'
    success_url = reverse_lazy('camera')

    def get_context_data(self, *args, **kwargs):
        context = super(PhotoUpdate, self).get_context_data(*args, **kwargs)
        context['cameras']=PhotoPerson.objects.all()
        return context


class PhotoDelete(DeleteView):
    model = PhotoPerson
    template_name = 'webcamapp/delete.html'
    success_url = reverse_lazy('camera')

    def get_context_data(self, *args, **kwargs):
        context = super(PhotoDelete, self).get_context_data(*args, **kwargs)
        context['cameras']=PhotoPerson.objects.all()
        return context
