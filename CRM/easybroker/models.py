from django.db import models

class EB_Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    username = models.TextField(max_length=50,unique=True)
    password = models.TextField(max_length=50)
    confirm_password = models.TextField(max_length=50)
