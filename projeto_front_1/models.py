from django.db import models


class PostagemModel(models.Model):
    ASSUNTO_CHOICES = [
        ('Assunto 1', 'Assunto 1'),
        ('Assunto 2', 'Assunto 2'),
        ('Assunto 3', 'Assunto 3'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    assunto = models.CharField(max_length=200, choices=ASSUNTO_CHOICES)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome