from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class RT(models.Model):
	user= models.ForeignKey(User)
	thought=models.CharField(max_length=300)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	public=models.BooleanField()

	def __str__(self):
		return self.thought