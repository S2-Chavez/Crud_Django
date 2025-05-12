from django.db import models

class Tarefas(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    descricao = models.TextField()
    creat_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)