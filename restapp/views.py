from django.shortcuts import render,redirect
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from django.views import generic
from .models import *
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
import os
from twilio.rest import Client
# from dotenv import load_dotenv
# load_dotenv()
import random




#
# phone_number=os.getenv("PHONE_NUMBER")
# account_sid=os.getenv("TWILIO_ACCOUNT_SSID")
# auth_token=os.getenv("TWILIO_AUTH_TOKEN")
# client=Client(account_sid,auth_token)







# class regclass(generic.CreateView):
#     serializer_class=RegisterSerializer
#     template_name="register.html"
#
#     if random_number==message.body:
#         success_url=reverse_lazy('log')
#     else:




# class reglass(generic.View):
#     message=None
#     serializer_class = RegisterSerializer
#     template_name = "register.html"
#     def get(self,request):
#         form=self.serializer_class
#         return render(request,'register.html',{'form':form})
#     def post(self,request):
#         if request.method=='POST':
#             a=RegisterSerializer(data=request.POST)
#             if a.is_valid():
#                 self.un=a.validated_data['username']
#                 self.em=a.validated_data['email']
#                 self.ph=a.validated_data['phno']
#                 self.ps=a.validated_data['password']
#                 self.cp=a.validated_data['confirm']
#                 if self.ps==self.cp:
#                     return redirect('send')
#
#
#
#
#
# class send(generic.View):
#     random_number = random.randint(1000, 9999)
#     print(random)
#     message = client.messages.create(
#         body=random_number,
#         from_="+14066604625",
#         to=phone_number
#     )
#     print(random_number,"//////")
#     print(message,"######")
#     def get(self,request):
#         return redirect('otp')
#
# class OtpView(send):
#     def get(self, request):
#         return render(request, "otp.html")
#     def post(self, request):
#         if request.method == "POST":
#             f = otpserializer(data=request.POST)
#             if f.is_valid():
#                 ot = f.validated_data['otp']
#                 if ot == self.message.body:
#                     user = RegisterModel(username=self.un, email=self.em, phno=self.ph, password=self.ps)
#                     user.save()
#                     return HttpResponse("registration success")
#                 return HttpResponse("failed")



























# Create your views here.
class Register(APIView):
    def post(self,request):
        serializers=RegisterSerializer(data=request.data)
        data={}
        if serializers.is_valid(raise_exception=True):
                account=serializers.save()


                random_number = random.randint(1000, 9999)
                print(random_number)
                message = client.messages.create(
                    body=random_number,
                    from_="+14066604625",
                    to=phone_number
                )
                print(random_number, "///////")
                print(message.body, "########")
                otp=Otp(user=account,otp=random_number)
                print(otp,"//////")
                otp.save()
                data['response']="otp sended  successfully"
        else:
            data=serializers.errors
        return Response(data)


class check(APIView):
    def post(self, request):
        serializer = checkSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data['user']
            otp = serializer.validated_data['otp']

            try:
                register_instance = RegisterModel.objects.get(username=name)
                otp_instance = Otp.objects.get(user=register_instance)
                if otp_instance.otp == otp:
                    return Response({"response": "success"})
                else:
                    return Response({"response": "failed"})
            except RegisterModel.DoesNotExist:
                return Response({"response": "failed"})

class loginview(APIView):
    def post(self,request):
            serializers = login(data=request.data)
            if serializers.is_valid():
                em=serializers.validated_data['email']
                ps=serializers.validated_data['password']
                obj=RegisterModel.objects.get(email=em)
                print(obj,"///////")
                if obj.password==ps:
                    return Response({"msg":"login success"})
                else:
                    return Response({"msg":"login failed"})
            else:
                return Response({"msg":"failed"})





#
# class itemlist(generics.ListCreateAPIView):
#     serializer_class = itemSerializer
#     def get_queryset(self):
#         queryset=ItemName.objects.all()
#         locations=self.request.query_params.get('locationName')
#         if locations is not None:
#             queryset=queryset.filter(itemlocation=locations)
#         return queryset
#
# class itemdetails(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = itemSerializer
#     queryset = ItemName.objects.all()
#
# class locationlist(generics.ListCreateAPIView):
#     serializer_class = locationSerializer
#     queryset = Location.objects.all()
#
# class locationdetails(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = locationSerializer
#     queryset = Location.objects.all()