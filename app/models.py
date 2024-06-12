from django.db import models

# Create your models here.
class Menu(models.Model):
    Id = models.AutoField
    name = models.CharField(max_length = 30)
    category = models.CharField(max_length = 20)
    sub_category = models.CharField(max_length = 20)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length = 300)
    Image = models.ImageField(upload_to='app/images', default='')

    def __str__(self):
        return self.name
    
class Menu_category(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30)
    category = models.CharField(max_length = 20)
    sub_category = models.CharField(max_length = 20)
    description = models.CharField(max_length = 300)
    Image = models.ImageField(upload_to='app/menu_category', default='')

    def __str__(self):
        return self.name
