from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField()
    answer = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

class StudentProgress(models.Model):
    student_id = models.CharField(max_length=255)  # unique student id
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
