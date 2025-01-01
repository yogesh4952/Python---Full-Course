from django.db import models

# Create your models here
class Author(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  data_of_birth = models.DateField()
  phone_number = models.BigIntegerField()
  email_address = models.EmailField()
  
  def __str__(self):
    return self.first_name + f"  {self.id}"



