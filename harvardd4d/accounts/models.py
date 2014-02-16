from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRole(models.Model):
    ROLE = (('coder','Coder'),('mentor','Mentor'),('sponsor','Sponsor'),('admin', 'System Administrator'))
    role = models.CharField(max_length=50, choices=ROLE)

    def __str__(self):
        return self.role

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    role = models.ForeignKey(UserRole, related_name='users')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
