from django.db import models

# product category model
class Product(models.Model):
    # This creates a dropdown menu for sizes
    SIZE_CHOICES = [
        ('33cl', '33cl Small'),
        ('50cl', '50cl Standard'),
        ('75cl', '75cl Large'),
        ('Dispenser', '19L Dispenser Jar'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/') # This is for your photos

    def __str__(self):
        return f"{self.name} - {self.size}"
