from django import forms
from .models import Project, ContentBox

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do projeto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descreva o propósito deste projeto (opcional)', 'rows': 3}),
        }

class ContentBoxForm(forms.ModelForm):
    class Meta:
        model = ContentBox
        fields = ['title', 'short_description', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do snippet ou anotação'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Breve resumo (opcional)'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cole aqui seu código ou escreva sua anotação...', 'rows': 10, 'style': 'font-family: monospace;'}),
        }
