from django.db import models
import datetime

class Rating(models.Model):
    good = models.IntegerField()
    average = models.IntegerField()
    bad = models.IntegerField()
    date = models.DateField()

def store_rating(good, average, bad):
    rating = Rating(good=good, average=average, bad=bad, date=datetime.date.today())
    rating.save()
    
class Login(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    