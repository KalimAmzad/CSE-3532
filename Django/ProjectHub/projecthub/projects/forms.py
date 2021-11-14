from django.forms import ModelForm
from .models import Projects


class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        exclude = ['project_priority_sl']
        # fields = ['title', 'description', 'demo_link', 'source_link']
        # fields = '__all__'
