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


class todo(models.Model):
  title = models.CharField(max_length=70)
  content = models.CharField(max_length=200)
  completion_status  = models.BooleanField()
  deadline_date = models.DateField()

  def __str__(self):
    return self.title + f"  {self.deadline_date}"



