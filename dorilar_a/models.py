from django.db import models

# Create your models here.


class Dori(models.Model):
    make = models.CharField(max_length=20)
    nomi = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    xususiyat = models.TextField()
    miqdori = models.PositiveIntegerField()
    chiqarilgan_vaqt = models.DateField(auto_now_add=True)
    tugash_muddati = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='dorilar/', blank=True, null=True)

    class Meta:
        ordering = ['-create_at']
        verbose_name = 'Dori'

    def __str__(self):
        return f'{self.make} {self.nomi}'
