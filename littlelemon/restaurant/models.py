from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    reservation_date = models.DateTimeField()
    reservation_slot = models.SmallIntegerField(default=10)

        
    def __str__(self): 
        return self.first_name