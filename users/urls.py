from django.urls import path

from users.views import registration, login
app_name = 'users'


urlpatterns = [
    path('registration/', registration, name='reg'),
    path('login/', login, name='login')
]
