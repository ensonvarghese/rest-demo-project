from django.db import models

# Create your models here.
class University(models.Model):
    university_name  = models.CharField(max_length=200,null=True,blank=True) 
    class Meta:
        verbose_name = ("University")
        verbose_name_plural = ("University")
    def __str__(self):
        return str(self.university_name) 

class Students(models.Model):
    name  = models.CharField(max_length=50,null=True,blank=True) 
    branch  = models.CharField(max_length=50,null=True,blank=True)
    univeristy = models.ForeignKey(University,related_name='uni',on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Studens")
    def __str__(self):
        return str(self.name)            
