from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import *

class HomePageView(TemplateView):
    template_name = "home.html"

class CharacterDetailView(DetailView):
    model = characterBase
    template_name = "characterDetail.html"
