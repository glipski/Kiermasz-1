# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models

# rejestrujemy modele w panelu administracyjnym
admin.site.register(models.Ksiazki)
