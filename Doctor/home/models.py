from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator , MaxValueValidator
from django.core.exceptions import ValidationError

class Patient(models.Model):
    doctor = models.ForeignKey(User , on_delete=models.CASCADE , related_name='pationts')
    full_name = models.CharField(max_length=255)
    feshar = models.BooleanField(default=False)   
    deyabet =  models.BooleanField(default=False)   
    tashanoj =  models.BooleanField(default=False)    
    other = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self) :
        return f'{self.full_name}-{self.doctor}'
 
    def get_total_price(self):
        total = sum(item.remaining_money() for item in self.items.all()) 
        return total
    
class PatientList(models.Model):
    petient = models.ForeignKey(Patient,on_delete=models.SET_NULL , null=True,related_name='items')
    created = models.DateField(auto_now_add=True)
    do = models.CharField(max_length=500)
    price = models.IntegerField()
    paid = models.IntegerField(validators=[MinValueValidator(0)],default=0)
    
    def clean(self) :
        if self.paid > self.price :
            raise ValidationError ({'paid': 'Paid amount cannot be greater than the price.'})
    
    def remaining_money(self):
        price = self.price if self.price is not None else 0
        paid = self.paid if self.paid is not None else 0
        return price - paid
    