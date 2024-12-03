from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()
    date_of_birth = models.DateField(null=True)  
    age = models.PositiveIntegerField(null=True)  

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        
        from datetime import date
        if self.date_of_birth:
            today = date.today()
            self.age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        super().save(*args, **kwargs)

