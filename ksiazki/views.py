# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def index(request):
    """Strona główna"""
    kontekst = {'komunikat': 'Witaj w aplikacji Ogłoszenia!'}
    return render(request, 'ksiazki/index.html', kontekst)


@method_decorator(login_required, 'dispatch')
class KsiazkiCreate(CreateView):

    model = models.Ksiazki
    form_class = forms.KsiazkiForm
    success_url = reverse_lazy('ksiazki:lista') # '/ksiazki/lista'

"""
    def get_context_data(self, **kwargs):
        context = super(KsiazkiCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['ksiazki'] = forms.KsiazkiFormSet(self.request.POST)
        else:
            context['ksiazki'] = forms.KsiazkiFormSet()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        ksiazki = forms.KsiazkiFormSet(self.request.POST)
        if form.is_valid() and ksiazki.is_valid():
            return self.form_valid(form, ksiazki)
        else:
            return self.form_invalid(form, ksiazki)

    def form_valid(self, form, ksiazki):
        form.instance.autor = self.request.user
        self.object = form.save()
        ksiazki.instance = self.object
        ksiazki.save()
        return HttpResponseRedirect(self.get_success_url())
"""
"""    def form_invalid(self, form, ksiazki):
        return self.render_to_response(
            self.get_context_data(form=form, skladniki=ksiazki)
        )
"""

@method_decorator(login_required, 'dispatch')
class KsiazkiUpdate(UpdateView):
    """Widok aktualizuacji"""

    model = models.Ksiazki
    form_class = forms.KsiazkiForm
    success_url = reverse_lazy('ksiazki:lista')  # '/ksiazki/lista'
"""
    def get_context_data(self, **kwargs):
        context = super(KsiazkiUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['ksiazki'] = forms.KsiazkiFormSet(
                self.request.POST,
                instance=self.object)
        else:
            context['ksiazki'] = forms.KsiazkiFormSet(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        ksiazki = forms.KsiazkiFormSet(
            self.request.POST,
            instance=self.object)
        if form.is_valid() and ksiazki.is_valid():
            return self.form_valid(form, ksiazki)
        else:
            return self.form_invalid(form, ksiazki)

    def form_valid(self, form, ksiazki):
        form.instance.autor = self.request.user
        self.object = form.save()
        ksiazki.save()
        return HttpResponseRedirect(self.get_success_url())
"""
"""    def form_invalid(self, form, ksiazki):
        return self.render_to_response(
            self.get_context_data(form=form, skladniki=ksiazki)
        )
"""
@method_decorator(login_required, 'dispatch')
class KsiazkiDelete(DeleteView):
    model = models.Ksiazki
    success_url = reverse_lazy('ksiazki:lista')  # '/ksiazki/lista'
"""
    def get_context_data(self, **kwargs):
        context = super(KsiazkiDelete, self).get_context_data(**kwargs)
        ksiazki = models.Ksiazki.objects.filter(ksiazki=self.object)
        context['ksiazki'] = ksiazki
        return context
"""
