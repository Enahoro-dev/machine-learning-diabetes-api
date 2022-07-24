from django.db import models

# Create your models here.

class User(models.Model):
    Name = models.CharField(null=False, blank=False, max_length=50)
    Email = models.EmailField(blank=False)
    Pregnancies = models.IntegerField(blank=False)
    Glucose  = models.IntegerField(blank=False)
    BloodPressure  = models.IntegerField(blank=False)
    SkinThickness  = models.IntegerField(blank=False)
    Insulin  = models.IntegerField(blank=False)
    BMI  = models.IntegerField(blank=False)
    DiabetesPedigreeFunction  = models.IntegerField(blank=False)
    Age = models.IntegerField(blank=False)
    Diagnosis = models.CharField(blank=False, max_length=50)