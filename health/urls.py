
from django.urls import path
from . import views
urlpatterns = [
   path('',views.hindex,name="hindexpage"),
   path('medical/',views.Medial,name="medical"),
   path('cosmatic/',views.Consmatic,name="cosmatic")
]