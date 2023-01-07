from django.shortcuts import render
from .forms import startupModelForm
from django.contrib.auth.models import User
from .models import startupModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
 
def startupFormView(request):
    context ={}
 
    form = startupModelForm(request.POST or None, request.FILES or None)
     
    if form.is_valid():
        form.save(commit=False)
        form.save()

    print(request.user)

    context['form']= form
    return render(request, "startups/startupForm.html", context)

class startupList(ListView):
    model = startupModel
    context_object_name = 'startups'


class startupDetail(DetailView):
    model = startupModel
    context_object_name = 'startup'