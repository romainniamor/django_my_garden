import json

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator, EmptyPage
from django.db import transaction
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.db.models.query_utils import Q

from .models import *
from .forms import *
from .filters import *

from django.core.mail import send_mail, BadHeaderError, EmailMessage




def index(request):
    context = {}
    return render(request, 'myapp/index.html', context)



def profile_list(request):

    profiles = Profile.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, 'myapp/profiles.html', context)



def register(request):
    user_form = CreateUserForm()
    profile_form = ProfileForm()

    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                profile_form = ProfileForm(request.POST, instance=profile)
                profile_form.save()
            else:
                profile_form = ProfileForm(request.POST, instance=profile)
                profile_form.save()


            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password1']
            user = authenticate(request, username=username, email=email, password=password)
            login(request, user)
            messages.success(request, 'Compte créé avec succès !')
            return redirect('/myapp/')
        else:
            user_form = CreateUserForm(request.POST)
            profile_form = ProfileForm(request.POST)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, "registration/register.html", context)




@login_required(login_url='/myapp/login/')
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Compte modifié avec succès !')
            return redirect('/myapp/')
        else:
            messages.success(request, '¡ Petite erreur de saisie, vérifiez et réessayez !')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required(login_url='/myapp/login/')
def delete_account(request):
    if request.method == 'POST':
        # suppression compte + deconnexion
        request.user.delete()
        logout(request)
        messages.success(request, 'Votre compte est supprimé. Merci et à bientôt!')
        return redirect('/myapp/')
    return render(request, 'registration/delete_account.html')

#changement de mdp via update_profil

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('myapp:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Mot de passe modifié avec succès!')
        return response


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Connexion de {username} réussie!')
            return redirect('/myapp/')
        else:
            messages.success(request, '¡ Petite erreur de saisie, vérifiez et réessayez !')

    context = {}
    return render(request, "registration/login.html", context)


def logout_user(request):
    username = request.user.username
    logout(request)
    messages.success(request, f'Déconnexion de {username} !')
    return redirect('/myapp/')



#renvoi de mdp par mail
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = CustomPasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            user_email = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=user_email))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Mot de passe oublié"
                    message = render_to_string("password/password_reset_email.html", {
                         'domain': get_current_site(request).domain,
                         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                         'token': default_token_generator.make_token(user),
                         'protocol': 'https' if request.is_secure() else 'http',
                        })
                    email = EmailMessage(subject, message, to=[user_email])
                    email.content_subtype = 'html'

                    try:
                        email.send()
                        print('envoi de email')
                        messages.success(request, 'Un message vous a été envoyé par mail. Suivez les instructions pour récupérer votre mot de passe.')
                    except BadHeaderError:
                        messages.error(request, 'Une erreur est survenue. Essayez ultérieurement!')
                    return redirect('/myapp/')

            else:
                messages.error(request, f'Adresse {user_email} incorrecte.')

    password_reset_form = CustomPasswordResetForm()
    return render(request=request,
                  template_name="password/password_reset.html",
                  context={"password_reset_form": password_reset_form})

#requetage des cartes produits avec pagination
def products(request):
    if request.user.is_authenticated:

        products = Produit.objects.all().exclude(nom='Divers').order_by('nom')
        product_filter = ProduitFilter(request.GET, queryset=products)

        if not product_filter.qs:
            context = {
                'message': "Désolé, aucun produit trouvé",
                'product_filter': product_filter,
            }
            return render(request, 'myapp/products.html', context)



        paginated_product = Paginator(product_filter.qs, 20)
        page_number = request.GET.get('page')
        page_obj = paginated_product.get_page(page_number)

        context = {
            'product_filter': product_filter,
            'page_obj': page_obj,

        }

        return render(request, 'myapp/products.html', context)

    else:
        messages.success(request, 'Connectez vous pour accéder aux produits.')
        return redirect('/myapp/login/')


#requetage et filtrage des cartes astuces
def tricks(request):
    if request.user.is_authenticated:
        tricks_filter = Tricks_Filter(request.GET, queryset=Conseil.objects.all())

        if not tricks_filter.qs:
            context = {
                'message': "Aucune astuce trouvée",
                'tricks_filter': tricks_filter,
            }
            return render(request, 'myapp/tricks.html', context)

        paginator = Paginator(tricks_filter.qs, 20)
        page_number = request.GET.get('page', 1)
        try:
            page_obj = paginator.get_page(page_number)
        except EmptyPage:
            page_obj = paginator.get_page(1)

        context = {
            'tricks_filter': tricks_filter,
            'page_obj': page_obj,
        }
        return render(request, 'myapp/tricks.html', context)

    else:
        messages.success(request, 'Connectez vous pour accéder aux astuces.')
        return redirect('/myapp/login/')





def garden(request):
    if request.user.is_authenticated:
        user = request.user.profile
        #selection pour l user connecté
        selection = Selection.objects.filter(profile=user)
        #identification du climat de user
        climat = request.user.profile.departement.id_region.id_climat

        # liste des id de produits dans la sélection
        produits_id = selection.values_list('produit_id', flat=True)

        # événements filtrer avec climat et produits sélectionnés
        events = Planning.objects.filter(climat=climat, produit_id__in=produits_id)

        # liste des element de l user dans sa collection
        collection = Collection.objects.filter(profile=user)



        context = {
            'selection': selection,
            'events': events,
            'collection': collection,
        }

        return render(request, 'myapp/my_garden.html', context)

    else:
        messages.success(request, 'Connectez vous pour accéder à votre jardin.')
        return redirect('/myapp/login/')


@login_required(login_url='/myapp/login/')
def update_selection(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    profile = request.user.profile
    product = Produit.objects.get(id=product_id)
    print('prod', product)

    climat = request.user.profile.departement.id_region.id_climat


    if action == 'add':
        selection, created = Selection.objects.get_or_create(profile=profile, produit=product)

        if created:
            message = 'Produit ajouté à votre jardin.'

        else:
            message = 'Ce produit est déjà dans votre jardin!'

        selection.save()
        return JsonResponse({'success': True, 'action': action, 'message': message})

    elif action == 'remove':
        Selection.objects.filter(profile=profile, produit=product).delete()
        message = 'Produit retiré du jardin!'

    selection = Selection.objects.filter(profile=profile)
    events = Planning.objects.filter(climat=climat, produit__in=[element.produit for element in selection])

    html = render_to_string(template_name='myapp/products_box_selection.html', context={'selection': selection, 'events': events})

    return JsonResponse({'success': True, 'action': action, 'message': message, 'html': html})



@login_required(login_url='/myapp/login/')
def update_calendar(request):
    data = json.loads(request.body)
    product_id = data['productId']
    product = Produit.objects.get(id=product_id)
    print('data', data, 'product', product_id, product)

    climat = request.user.profile.departement.id_region.id_climat
    events = Planning.objects.filter(climat=climat, produit=product)
    profile = request.user.profile
    selection = Selection.objects.filter(profile=profile)
    html = render_to_string(template_name='myapp/calendar.html', context={'events': events, 'selection': selection})
    print(html)

    events_json = []
    for event in events:
        events_json.append({
            'name': str(event.evenement), #bien penser a convertir event en chaine de caractere!!!
            'startDate': event.date_deb,
            'endDate': event.date_fin,
        })
        print('events', events_json)

    return JsonResponse({'success': True, 'html': html, 'events': events_json})


@login_required(login_url='/myapp/login/')
def update_collection(request):
    data = json.loads(request.body)
    trick_id = data['trickId']
    action = data['action']

    profile = request.user.profile

    trick = Conseil.objects.get(id=trick_id)


    if action == 'add':
        collection, created = Collection.objects.get_or_create(profile=profile, conseil=trick)

        if created:
            message = 'Carte ajoutée à votre jardin.'

        else:
            message = 'Carte déjà ajoutée dans votre jardin!'

        collection.save()

        return JsonResponse({'success': True, 'action': action, 'message': message})

    elif action == 'remove':
        Collection.objects.filter(profile=profile, conseil=trick).delete()
        message = 'Carte retirée du jardin!'

    collection = Collection.objects.filter(profile=profile)

    html = render_to_string('myapp/tricks_box_collection.html', {'collection': collection})

    return JsonResponse({'success': True, 'action': action, 'message': message, 'html': html}, safe=False)










