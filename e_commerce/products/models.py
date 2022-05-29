from django.db import models

# Create your models here.
class Products(models.Model):
    Name = models.CharField(max_length = 200)
    description = models.TextField()
    price = models.IntegerField()
    summary = models.TextField()

    def __str__(self):
        return (self.Name)
        



    class Meta:
        verbose_name_plural = "products"

