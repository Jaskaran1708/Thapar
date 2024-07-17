from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from app.views import (
    CreateUserView,
    RetrieveUserView,
    CreateContactView,
    RetrieveContactView,
    CreateSpamView,
    RetrieveSpamView,
    SearchByNameView,
    SearchByPhoneView
)

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='create_user'),
    path('users/<int:pk>/', RetrieveUserView.as_view(), name='retrieve_user'),
    path('contacts/', CreateContactView.as_view(), name='create_contact'),
    path('contacts/<int:pk>/', RetrieveContactView.as_view(), name='retrieve_contact'),
    path('spamreports/', CreateSpamView.as_view(), name='create_spam'),
    path('spamreports/<int:pk>/', RetrieveSpamView.as_view(), name='retrieve_spam'),
    path('search/name/<str:data>/', SearchByNameView.as_view(), name='search_by_name'),
    path('search/number/<str:number>/', SearchByPhoneView.as_view(), name='search_by_phone'),
]







# from django.contrib import admin
# from django.urls import path
# from app.views import (
#     CreateUserView,
#     RetrieveUserView,
#     CreateContactView,
#     RetrieveContactView,
#     CreateSpamView,
#     RetrieveSpamView, 
#     SearchByNameView, 
#     SearchByPhoneView
# )

# urlpatterns = [
#     path('users/', CreateUserView.as_view(), name='create-user'),
#     path('users/<int:pk>/', RetrieveUserView.as_view(), name='user-detail'),
#     path('contacts/', CreateContactView.as_view(), name='create-contact'),
#     path('contacts/<int:pk>/', RetrieveContactView.as_view(), name='contact-detail'),
#     path('spamreports/', CreateSpamView.as_view(), name='creat-spam'),
#     path('spamreports/<int:pk>/', RetrieveSpamView.as_view(), name='spamreport-detail'),
#     path('search/<str:data>/', SearchByNameView.as_view(), name='search-by-name'),
#     path('search/number/<str:number>/', SearchByPhoneView.as_view(), name='search-by-phone'),
# ]
