from .models import Profile, Fren
# from django.contrib.auth.models import User

def add_profiles(request):
    profiles = Profile.objects.all()
    return { 'profiles': profiles, }

def add_frens(request):
    frens = Fren.objects.all()
    return { 'frens': frens }