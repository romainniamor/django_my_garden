from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Climat(models.Model):
    id_climat = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'climat'

    def __str__(self):
        return self.nom

class Region(models.Model):
    id_region = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=30, blank=True, null=True)
    id_climat = models.ForeignKey(Climat, models.DO_NOTHING, db_column='id_climat', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'region'

    def __str__(self):
        return self.nom

class Departement(models.Model):
    id_departement = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)
    id_region = models.ForeignKey(Region, models.DO_NOTHING, db_column='id_region', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'departement'

    def __str__(self):
        return self.nom


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, models.DO_NOTHING, db_column='id_departement', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'profile'

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if not instance.is_staff:
        instance.profile.save()



class Produit(models.Model):
    SEASONS = [
        ('été', 'Eté'),
        ('printemps', 'Printemps'),
        ('automne', 'Automne'),
        ('hiver', 'Hiver'),
    ]


    nom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    besoin_eau = models.SmallIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(3)])
    besoin_soleil = models.SmallIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(3)])
    saison = models.CharField(choices=SEASONS, max_length=30, blank=True, null=True)
    image = models.ImageField( null=True, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        managed = True
        db_table = 'produit'


class Conseil(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=600, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        managed = True
        db_table = 'conseil'


class Selection(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.profile.user.username

    class Meta:
        managed = True
        db_table = 'selection'

class Collection(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    conseil = models.ForeignKey(Conseil, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.profile.user.username

    class Meta:
        managed = True
        db_table = 'collection'


class Evenement(models.Model):
    nom = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        managed = True
        db_table = 'evenement'


class Planning(models.Model):
    climat = models.ForeignKey(Climat, models.DO_NOTHING, db_column='id_climat', blank=True, null=True)
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, blank=True, null=True)
    evenement = models.ForeignKey(Evenement, on_delete=models.SET_NULL, blank=True, null=True)
    date_deb = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.produit)


    class Meta:
        managed = True
        db_table = 'planning'
















