from django.forms import ModelForm
from .models import Theme

class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'description', 'favorite_color', 'upload'] # or '__all__'