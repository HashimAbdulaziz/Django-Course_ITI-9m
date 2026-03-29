from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True) 
    email = models.EmailField()
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    
    # I don't need but it's to make quering faster
    subjects = models.ManyToManyField('Subject', through='Grade')
    
    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Grade(models.Model):
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        score_display = self.score if self.score is not None else "Not Graded"
        return f"{self.student.name} - {self.subject.name}: {score_display}"



class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.email}"