import django_filters
from django_filters import FilterSet, CharFilter, ChoiceFilter
from .models import *
from django import forms


class ProduitFilter(django_filters.FilterSet):
    SAISON_CHOICES = (
        ('été', 'Eté'),
        ('automne', 'Automne'),
        ('hiver', 'Hiver'),
        ('printemps', 'Printemps'),
    )
    saison = ChoiceFilter(choices=SAISON_CHOICES, empty_label="Saison", label='Saison')
    nom = CharFilter(lookup_expr='icontains', label='Produit', widget=forms.TextInput(attrs={'placeholder': 'Rechercher un produit...'}))

    class Meta:
        model = Produit
        fields = ['saison', 'nom']

class Tricks_Filter(django_filters.FilterSet):
    produit = django_filters.ModelChoiceFilter(label="Liste des produits", empty_label="Liste des produits", queryset=Produit.objects.all().order_by('nom'))
    class Meta:
        model = Conseil
        fields = ['produit']



