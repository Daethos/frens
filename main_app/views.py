from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fren, Profile 
from django.views.generic import ListView
from .forms import ThemeForm 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profiles_index(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/index.html', { 'profiles': profiles })

def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    theme_form = ThemeForm()
    return render(request, 'profiles/detail.html', { 
        'profile': profile, 'theme_form': theme_form 
    })

def frens_index(request):
    frens = Fren.objects.all()
    return render(request, 'frens/index.html', { 'frens': frens})

def frens_detail(request, fren_id):
    fren = Fren.objects.get(id=fren_id)
    return render(request, 'frens/detail.html', { 'fren': fren })

class ProfileCreate(CreateView):
    model = Profile
    fields = ['name', 'age', 'description'] # no more __all__ to bypass frenships
    success_url = '/profiles/'

class ProfileUpdate(UpdateView):
    model = Profile
    fields = '__all__'

class ProfileDelete(DeleteView):
    model = Profile
    success_url = '/profiles/'

def add_theme(request, profile_id):
    form = ThemeForm(request.POST)
    if form.is_valid():
        new_theme = form.save(commit=False)
        new_theme.profile_id = profile_id
        new_theme.save()
    return redirect('detail.profile', profile_id)

def request_fren(request, profile_id, fren_id):
    Profile.objects.get(id=profile_id).frens.add(fren_id)
    return redirect('detail.profile', profile_id=profile_id)