from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_, name='login'),
    path('signup', views.signup, name = 'signup'),
    path('home/', views.home, name = 'home'),
    path('about-us/', views.aboutus, name = 'about-us'),
    path('muscle/', views.MuscleView.as_view(), name = 'muscle'),
    path('muscles/<int:muscle_id>/', views.SubMuscleView.as_view(), name='submuscle'),
    # path('exercises/<int:sub_muscle_id>/', views.ExerciseView.as_view(), name='exercise'),
    path('submit_complaints/', views.submit_complaint, name = 'complaint'),
    path('complaints/', views.complaint_lists, name = 'complaint_list'),
    path('membership_status/', views.membership_status, name = 'membership'),
    # path('chest/', views.chest, name = 'chest'),
    # path('back/', views.back, name = 'back'),
    # path('shoulder/', views.shoulder, name = 'shoulder'),
    # path('biceps/', views.biceps, name = 'biceps'),
    # path('triceps/', views.triceps, name = 'triceps'),
    # path('abs/', views.abs, name = 'abs'),
    # path('legs/', views.legs, name = 'legs'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('payment/', views.payment.as_view(), name = 'payment'),
    path('successfull/', views.Payment_successful, name = 'successfull'),

    # Add more URL patterns as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)