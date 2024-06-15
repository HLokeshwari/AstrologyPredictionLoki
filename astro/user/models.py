from django.db import models

# Create your models here.

gender_choices={
    ('Male','Male'),('Female','Female'),('prefer not to say','Prefer Not To Say')
}

class register(models.Model):
    name=models.CharField(max_length=100,blank=False)
    gender=models.CharField(max_length=100,blank=False,choices=gender_choices)
    email=models.EmailField(max_length=100,blank=False)
    username=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=100,blank=False)
    contact=models.BigIntegerField(blank=False)
    registrationtime=models.DateTimeField(blank=False,auto_now=True)

    class Meta:
        db_table='registration_table'

    def __str__(self):
        return self.name
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    query = models.TextField()

    def _str_(self):
        return self.name



