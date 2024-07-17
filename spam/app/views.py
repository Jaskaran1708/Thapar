from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Contact, SpamReport, CustomUser
from .serializers import UserSerializer, ContactSerializer, SpamReportSerializer
from django.db.models import Count
from rest_framework.exceptions import ValidationError

class CreateUserView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        phone_number = serializer.validated_data.get('phone_number')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise ValidationError({'phone_number': 'A user with this phone number already exists.'})
        serializer.save()

class RetrieveUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class CreateContactView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class RetrieveContactView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CreateSpamView(generics.ListCreateAPIView):
    queryset = SpamReport.objects.all()
    serializer_class = SpamReportSerializer

    def perform_create(self, serializer):
        serializer.save()

class RetrieveSpamView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpamReport.objects.all()
    serializer_class = SpamReportSerializer

class SearchByNameView(generics.GenericAPIView):
    def get_queryset(self):
        # query = self.GET['name']
        # print(query)
        return CustomUser.objects.none()

    def get(self, request, data, ):
        # query = request.GET['jassi']
        print(data)
        results = CustomUser.objects.filter(username__icontains=data).annotate(
            spam_count=Count('spamreport')
        ).order_by('-username', 'username')
        serializer = UserSerializer(results, many=True)
        return Response(serializer.data)
    
from rest_framework import generics
from rest_framework.response import Response
from .models import CustomUser, Contact
from .serializers import UserSerializer, ContactSerializer

class SearchByPhoneView(generics.GenericAPIView):
    def get(self, request, number):
        try:
            print(f"Searching for phone number: {number}")
            results = CustomUser.objects.filter(phone_number=number)
            if results.exists():
                serializer = UserSerializer(results, many=True)
            else:
                print(f"No CustomUser found with phone number: {number}, checking contacts")
                results = Contact.objects.filter(phone_number=number)
                serializer = ContactSerializer(results, many=True)
            
            print(f"Search results: {serializer.data}")
            return Response(serializer.data)
        except Exception as e:
            print(f"Error occurred: {e}")
            return Response({"error": str(e)}, status=500)


# class SearchByPhoneView(generics.GenericAPIView):
#     def get_queryset(self):
#         # query = self.GET['name']
#         # print(query)
#         return CustomUser.objects.none()

#     def get(self, request,number):
        
#         results = CustomUser.objects.filter(phone_number=number)
#         if not results.exists():
#             results = Contact.objects.filter(phone_number=number)
#         serializer = ContactSerializer(results, many=True)
#         return Response(serializer.data)


      
