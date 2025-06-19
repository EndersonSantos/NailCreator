from django import forms


class NailForm(forms.Form):
    description = forms.CharField(
        label='Descrição',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cores, tema, formato...'})
    )
    feelings = forms.CharField(
        label='Sentimentos (opcional)',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Poderosa, confiante...'})
    )
    count = forms.IntegerField(
        label='Quantidade de imagens',
        min_value=1,
        max_value=4,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
