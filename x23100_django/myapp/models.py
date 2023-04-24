from django.db import models

# Create your models here.
# defaul = not null
class User(models.Model):
    user_code = models.PositiveIntegerField(primary_key = True, blank = False, null = False)
    user_name = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)