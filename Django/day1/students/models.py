from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    

class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)