from django.contrib import admin
from .models import *

#https://docs.djangoproject.com/fr/3.2/ref/contrib/admin/#django.contrib.admin.AdminSite


#  user: admin
#  password: admin

#parametre d'en-tete de l'admin
admin.site.site_title = "My_Garden_Admin"
admin.site.site_header = "My_Garden"
admin.site.index_title = "Accueil"
# #admin.site.register(class_model) pr visuel de base

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'departement')
    search_fields = ['user__username', 'user__email']

    def email(self, obj):
        return obj.user.email

    email.admin_order_field = 'user__email'
    email.short_description = 'Email'


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'saison')
    ordering = ('saison', )
    search_fields = ('nom', 'saison')
    list_filter = ('nom',)


admin.site.register(Evenement)


@admin.register(Planning)
class PlanningAdmin(admin.ModelAdmin):
    list_display = ('produit', 'climat', 'evenement', 'date_deb', 'date_fin')
    list_filter = ('produit', 'climat', 'evenement')
    ordering = ('produit',)


@admin.register(Conseil)
class ConseilAdmin(admin.ModelAdmin):
    list_display = ('nom', 'produit')
    list_filter = ('produit',)

@admin.register(Selection)
class SelectionAdmin(admin.ModelAdmin):
    list_display = ('profile', 'produit')
    list_filter = ('profile',)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('profile', 'conseil')
    list_filter = ('profile',)







