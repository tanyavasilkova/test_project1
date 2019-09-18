from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Category
from .forms import CategoryCreateForm


class CategoryList(ListView):
    model = Category


class CategoryDetail(DetailView):
    model = Category


class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryCreateForm


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryCreateForm




