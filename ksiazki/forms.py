# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from . import models
from django.forms.models import inlineformset_factory


class KsiazkiForm(ModelForm):

    class Meta:
        model = models.Ksiazki
        exclude = ('#','data')
        widgets = {'opis': Textarea(attrs={'rows': 1, 'cols': 50}),
        'kontakt': Textarea(attrs={'rows': 1, 'cols': 50}),
        'wydawnictwo': Textarea(attrs={'rows': 1, 'cols': 50}),
        'autor': Textarea(attrs={'rows': 1, 'cols': 50}),
        'przedmiot': Textarea(attrs={'rows': 1, 'cols': 50}),
        'tytul': Textarea(attrs={'rows': 1, 'cols': 50}),
        }


"""KsiazkiFormSet = inlineformset_factory
    parent_model=models.Ksiazki,
    max_num=7,
    min_num=1,
    validate_max=True,
    validate_min=True,
    extra=2,
    fields=('tytul','autor')
)

"""
