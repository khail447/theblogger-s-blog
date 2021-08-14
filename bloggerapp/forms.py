from django.forms import ModelForm
from .models import Comment

class commentform(ModelForm):
    class Meta:
        model=Comment
        fields= ['name', 'body']