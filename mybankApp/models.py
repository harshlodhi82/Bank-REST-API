from django.db import models
from django.urls import reverse

# Create your models here.
class Bank(models.Model):
    ifsc = models.CharField(max_length = 50)
    bank_name = models.CharField(max_length = 100)
    branch = models.CharField(max_length = 50)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 50)
    district = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)

    def __str__(self):
        temp_str = self.bank_name[:10] + "-" + self.ifsc[:50]
        return temp_str

    # def get_absolute_url(self): # new
    #     return reverse('Bank', args=[self.ifsc])