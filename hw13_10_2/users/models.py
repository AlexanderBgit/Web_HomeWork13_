from django.db import models

# Create your models here.



# models.py
# реалізація на перспективу
# не є вимогою дамашнього завдання 
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


# @receiver(post_save, sender=User)
# def update_password(sender, instance, created, **kwargs):
#     if not created and instance.password:
#         print(f"Password for user {instance.username} has been changed.")

# # конект сигналу до User
# post_save.connect(update_password, sender=User)
