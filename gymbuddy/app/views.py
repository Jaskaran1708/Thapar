from django.shortcuts import render, get_object_or_404
from .form import CustomerProfileForm
from .models import *
from django.views.generic import View
from django.contrib import messages
from django.conf import settings
import stripe
from django.views.generic import TemplateView


def login(request):
    return render(request, 'app/login.html')

def signup(request):
    return render(request, 'app/signup.html')

def home(request):
    return render(request, 'app/home.html')

def aboutus(request):
    return render(request, 'app/about us.html')

def exercises(request):
    return render(request, 'app/exercises.html')

def chest(request):
    return render(request, 'app/chest.html')

def back(request):
    return render(request, 'app/back.html')

def shoulder(request):
    return render(request, 'app/shoulders.html')

def biceps(request):
    return render(request, 'app/biceps.html')

def triceps(request):
    return render(request, 'app/triceps.html')

def legs(request):
    return render(request, 'app/legs.html')

def abs(request):
    return render(request, 'app/abs.html')

class ProfileView(View):
 def get(self,request):
  form = CustomerProfileForm()
  return render(request, 'app/profile.html', {'form': form , 'active' : 'btn-primary'})
 def post(self,request):
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
   usr = request.user
   email = form.cleaned_data['email']
   first_name = form.cleaned_data['first_name']
   last_name = form.cleaned_data['last_name']
   phone_number = form.cleaned_data['phone_number']
   reg = Customer(user = usr,email = email, first_name = first_name, last_name = last_name, phone_number = phone_number)
   reg.save()
   messages.success(request, 'Congratulation!! Profile updated successfully')
  return render(request, 'app/profile.html', {'form' : form, 'active'  : 'btn-primary'})
 
class payment(TemplateView):
    template_name = 'app/payment.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context
    

def Payment_successful(request):
    if request.method == "POST":
        stripe.api_key = settings.STRIPE_SECRET_KEY
        charge = stripe.Charge.create(amount = 100,
          currency = 'inr',
          description = ' Payment ',
          source = request.POST['stripeToken']
          )
          
    return render(request, 'app/payment_successful.html')

class MuscleView(View):
    template_name = 'app/muscle.html'
    def get(self,request):
       muscles = Muscle.objects.all()
       return render(request, self.template_name, {'muscles': muscles})
    
class SubMuscleView(View):
    template_name = 'app/submuscle.html'

    def get(self, request, muscle_id):
        muscle = get_object_or_404(Muscle, id=muscle_id)
        sub_muscles = muscle.sub_muscles.all()
        return render(request, self.template_name, {'muscle': muscle, 'sub_muscles': sub_muscles})
    
class ExerciseView(View):
    template_name = 'app/submuscle.html'

    def get(self, request, sub_muscle_id):
        sub_muscle = get_object_or_404(SubMuscle, id=sub_muscle_id)
        exercises = sub_muscle.exercises.all()
        return render(request, self.template_name, {'sub_muscle': sub_muscle, 'exercises': exercises})

   