from django.db import models
from accounts.models import UserProfile

def content_file_name(instance, filename):
    return '/'.join(['orgs', instance.name, filename])

class Tag(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

# Create your models here.
class Partner(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()
    logo = models.FileField(upload_to=content_file_name, blank=True)
    picture = models.FileField(upload_to=content_file_name, blank=True)
    video = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1500)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
    	return self.name

class JobOpportunity(models.Model):
	partner = models.ForeignKey('Partner', related_name='jobopportunities')
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=3000)
	deadline = models.DateTimeField(null=True, blank=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=100)
	partner = models.ForeignKey('Partner', related_name='projects')
	users = models.ManyToManyField(UserProfile)
	problem = models.CharField(max_length=3000)
	proposal = models.CharField(max_length=5000)
	picture = models.FileField(upload_to=content_file_name)
	video = models.CharField(max_length=100, blank=True)
	timeline = models.CharField(max_length=1000)
	Project_STAGES = (('research', 'Research'), ('ideas', 'Ideas'), ('prototype', 'Prototype'), ('feedback', 'Feedback'), ('deployment', 'Deployment'))
	stage = models.CharField(max_length=20, choices=Project_STAGES)	
	tags = models.ManyToManyField(Tag)

	def __str__(self):
    		return self.name
