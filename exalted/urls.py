from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name="homePageView"),
    path('character/<pk>', CharacterDetailView.as_view(), name="characterDetailView"),
]
