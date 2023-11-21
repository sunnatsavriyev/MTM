from django.db import models
from django.db.models.signals import post_save
from django.dispatch import Signal
from django.contrib.auth.models import User



class KiderModel(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return str(self.username)

class Kider(models.Model):
    manzil=(
            ('Toshkent','Toshkent'),
            ('Toshkent','Toshkent vil'),
            ('Andijon','Andijon vil'),
            ('Buxoro','Buxoro vil'),
            ('Farg\'ona','Farg\'ona vil'),
            ('Jizzax','Jizzax vil'),
            ('Xorazm','Xorazm vil'),
            ('Namangan','Namangan vil'),
            ('Navoiy','Navoiy vil'),
            ('Qashqadaryo','Qashqadaryo vil'),
            ('Qoraqalpog\'iston','Qoraqalpog\'iston Res'),
            ('Samarqand','Samarqand vil'),
            ('Sirdaryo','Sirdaryo vil'),
            ('Surxondaryo','Surxondaryo vil'),
    )
    user = models.ForeignKey(KiderModel, on_delete=models.CASCADE, null=True)
    vasiyni_ismi = models.CharField(max_length=100)
    vasiyni_email = models.EmailField(max_length=250)
    farzand_ismi = models.CharField(max_length=100)
    farzand_yoshi = models.IntegerField(null=True, blank=True)
    tel_nomer = models.IntegerField(null=True, blank=True)
    joylashuv = models.CharField(blank=True, choices=manzil, null=True, max_length=200,default='Toshkent')
    xabar = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.vasiyni_ismi


def  create_profil(sender,instance, created, **kwargs):
    if created:
        KiderModel.objects.create(
            username=instance
        )
    else:
        profilemodel = KiderModel.objects.get(username=instance)
        profilemodel.email = instance.email
        profilemodel.name = instance.username 
        profilemodel.save()
        
Signal.connect(post_save,create_profil,sender=User)