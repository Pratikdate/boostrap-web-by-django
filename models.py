from django.db import models

# Create your models here.
class post(models.Model):
    sno=models.AutoField(primary_key=True)
    auther=models.CharField(max_length=12)
    tital=models.CharField(max_length=12)
    img=models.TextField()
    
    containt=models.TextField()
    
    slug=models.CharField(max_length=120)
    date=models.DateField()
    
    
    def __str__(self):
        return self.auther