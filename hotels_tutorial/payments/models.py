from django.db import models

# Create your models here.


class Person(models.Model):

    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100,null=False, blank=False)
    birthday = models.DateTimeField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.first_name