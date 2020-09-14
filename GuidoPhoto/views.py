from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import UPhoto
from .forms import UPhotoForm
from typing import Any, Type


class HomeView(ListView):
    model: Type[UPhoto] = UPhoto
    template_name: str = 'home.html'


class UploadView(CreateView):
    model: Type[UPhoto] = UPhoto
    form_class: Type[UPhotoForm] = UPhotoForm
    template_name: str = 'upload.html'
    success_url: Any = reverse_lazy('home')
