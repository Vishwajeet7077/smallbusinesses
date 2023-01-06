from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Event
# Create your views here.

class EventList(ListView):
    model = Event
    context_object_name = 'events'
    
class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'

class EventCreate(CreateView):
    model = Event
    fields = '__all__'
    context_object_name = 'event'
    success_url = reverse_lazy('events')

class EventUpdate(UpdateView):
    model = Event
    fields = '__all__'
    context_object_name = 'event'
    success_url = reverse_lazy('events')

class EventDelete(DeleteView):
    model = Event
    fields = '__all__'
    context_object_name = 'event'
    success_url = reverse_lazy('events')