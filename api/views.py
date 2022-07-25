from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.core.mail import send_mail
from .models import User
from .serializers import UserSerializer
import pickle

@api_view(['GET'])
def getRoute(request):
    return Response('Diabetes Api')

@api_view(['GET'])
def getUsers(request):
    users=User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def makeDiagnosis(request):
    data = request.data

    name = data['Name']
    email = data['Email']
    pregnancies = int(data['Pregnancies'])
    glucose  = int(data['Glucose'])
    pressure  = int(data['BloodPressure'])
    thickness  = int(data['SkinThickness'])
    insulin  = int(data['Insulin'])
    bmi  = int(data['BMI'])
    pedigree  = int(data['DiabetesPedigreeFunction'])
    age  = int(data['Age'])

    diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

    input_list = [pregnancies, glucose, pressure, thickness, insulin, bmi, pedigree, age]
    prediction= diabetes_model.predict([input_list])

    if prediction[0]==0:
        res = 'you are unlikely to have diabetes'
    else:
        res = 'you are at an increased risk of having diabetes'

    user = User.objects.create(
        Name = name,
        Email = email,
        Pregnancies = pregnancies,
        Glucose  = glucose,
        BloodPressure  = pressure,
        SkinThickness  = thickness,
        Insulin  = insulin,
        BMI  = bmi,
        DiabetesPedigreeFunction  = pedigree,
        Age  = age,
        Diagnosis = res
    )
    serializer = UserSerializer(user, many=False) 

    subject = 'DIABETES ASSESSMENT'
    message = f'    Hi {name}, we would like to inform you of the results of your recent online assessment which are that: {res}.\n  We hope that you would still seek medical evaluation as these results are highly subjective.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail( subject, message, email_from, recipient_list )
   
    return Response(res)  
