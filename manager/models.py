from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-created_at']

class ContentBox(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    short_description = models.CharField(max_length=255, verbose_name="Descrição Curta", blank=True)
    content = models.TextField(verbose_name="Conteúdo Completo (Snippet/Anotação)")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='content_boxes', verbose_name="Projeto")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Caixinha"
        verbose_name_plural = "Caixinhas"
        ordering = ['-created_at']
