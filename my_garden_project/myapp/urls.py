from django.urls import path
from . import views
from .views import CustomPasswordChangeView

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/', views.profile_list, name='profiles'),
    path('products/', views.products, name='products'),
    path('tricks/', views.tricks, name='tricks'),


    path('my_garden/', views.garden, name='my_garden'),
    path('update_selection/', views.update_selection, name='update_selection'),
    path('update_collection/', views.update_collection, name='update_collection'),
    path('update_calendar/', views.update_calendar, name='update_calendar'),

    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete_account/', views.delete_account, name='delete_account'),

    path('update_profile/', views.update_profile, name='update_profile'),
    path('password/', CustomPasswordChangeView.as_view(template_name='registration/update_password.html')),
    path('password_reset/', views.password_reset_request, name='password_reset'),

]

