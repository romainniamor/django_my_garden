from datetime import date

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import *
# Create your tests here.


class ClimatModelTest(TestCase):
    def setUp(self):
        Climat.objects.create(nom='Tropical')

    def test_climat_max_length(self):
        climat = Climat.objects.get(id_climat=1)
        max_length = climat._meta.get_field('nom').max_length
        self.assertEqual(max_length, 20)


class DepartementModelTest(TestCase):
    def setUp(self):
        Departement.objects.create(nom='nouveau departement')

    def test_departement_max_length(self):
        departement = Departement.objects.get(id_departement=1)
        max_length = departement._meta.get_field('nom').max_length
        self.assertEqual(max_length, 30)



class TestUserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='user_test', email='user_test@test.com', password='password')

    def test_user_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'nom d’utilisateur')

    def test_user_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 150)



class TestProfileModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(user='user_test', departement='nouveau_departement')


class ProduitModelTest(TestCase):

    def test_product_name_field(self):
        produit = Produit(nom="Tomate")
        field_label = produit._meta.get_field('nom').verbose_name
        self.assertEqual(field_label, "nom")

    def test_description_field(self):
        produit = Produit(description="Description de la tomate")
        self.assertEqual(produit.description, "Description de la tomate")

    def test_water_needs_field(self):
        produit = Produit(besoin_eau=2)
        self.assertEqual(produit.besoin_eau, 2)

    def test_sun_needs_field(self):
        produit = Produit(besoin_soleil=3)
        self.assertEqual(produit.besoin_soleil, 3)

    def test_season_field(self):
        produit = Produit(saison='été')
        self.assertEqual(produit.saison, 'été')



class Evenement_Model_Test(TestCase):
    def test_name_event_field(self):
        event = Evenement.objects.create(nom='recolte')
        field_label = event._meta.get_field('nom').verbose_name
        self.assertEqual(field_label, 'nom')

class PlanningModelTest(TestCase):
    def setUp(self):
        climat = Climat.objects.create(nom="tempéré")
        produit = Produit.objects.create(nom='tomate', besoin_eau=2, besoin_soleil=2, saison='été')
        evenement = Evenement.objects.create(nom='semis')
        self.planning = Planning.objects.create(climat=climat, produit=produit, evenement=evenement, date_deb=date.today(), date_fin=date.today())

    def test_planning_str(self):
        self.assertEqual(str(self.planning), 'tomate')

    def test_planning_climat(self):
        climat = Climat.objects.get(nom='tempéré')
        self.assertEqual(self.planning.climat, climat)

    def test_planning_productt(self):
        produit = Produit.objects.get(nom='tomate')
        self.assertEqual(self.planning.produit, produit)

    def test_planning_event(self):
        evenement = Evenement.objects.get(nom='semis')
        self.assertEqual(self.planning.evenement, evenement)

    def test_planning_date_start(self):
        self.assertEqual(self.planning.date_deb, date.today())

    def test_planning_date_end(self):
        self.assertEqual(self.planning.date_fin, date.today())




























