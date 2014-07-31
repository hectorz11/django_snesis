from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	def url(self,filename):
		ruta = "MultimediaData/Users/%s/%s"%(self.user.username,filename)
		return ruta

	user = models.OneToOneField(User)	
	photo = models.ImageField(upload_to=url)
	telefono = models.CharField(max_length=30)

	def __unicode__(self):
		return self.user.username

class Backup(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	observacion = models.TextField(max_length=750,null=True)
	userProfile = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return self.observacion