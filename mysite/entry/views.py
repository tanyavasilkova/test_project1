from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Note
from .forms import NoteCreateForm


class NoteList(ListView):
    model = Note


class NoteDetail(DetailView):
    model = Note


class NoteCreate(CreateView):
    model = Note
    form_class = NoteCreateForm






