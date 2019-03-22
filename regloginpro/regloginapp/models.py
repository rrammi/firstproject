from django.db import models

class RegistrationData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    number = models.BigIntegerField()
    def __str__(self):
        return self.first_name
