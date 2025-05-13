from django.db import models

class Tarefas(models.Model):
    title      = models.CharField('Título', max_length=255)
    descricao  = models.TextField('Descrição', blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.title
