from django import forms
from .models import PostagemModel

class PostagemForm(forms.ModelForm):
    assunto = forms.ChoiceField(
        choices=PostagemModel.ASSUNTO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = PostagemModel
        fields = ['nome', 'email', 'telefone', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }