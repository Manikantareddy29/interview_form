from django.db import models
from django.core.exceptions import ValidationError

class Booking (models.Model):

    ful_name = models.CharField(max_length=50)
    Employee_id = models.IntegerField(max_length=15)
    interview_start_time  = models.TimeField()
    interview_end_time  = models.TimeField()
    hr_number = models.IntegerField(max_length=15)
    hr_mail_id  = models.EmailField()
    hr_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    interview_round =  models.CharField(max_length=50)
    STATUS_CHOICES = [
        ('Done', 'Done'),
        ('ToDo', 'ToDo'),
        ('Rescheduled', 'Rescheduled'),
    ]

    DOMAIN_CHOICES = [
        ('Python', 'Python'),
        ('Data Engineering', 'Data Engineering'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    duration = models.TimeField()  # Duration is only required if status is 'Done'
    domain = models.CharField(max_length=20, choices=DOMAIN_CHOICES)
    def clean(self):
        if self.status == 'Done' and self.duration is None:
            raise ValidationError({'duration': 'Duration is required when status is "Done".'})
    
    def __str__(self):
        return self.Employee_id
