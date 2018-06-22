from django.db import models

# Create your models here.
class Facebook(models.Model):
	username=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	img=models.ImageField(null=True)

	def __str__(self):
		return self.username
	class Meta:
		verbose_name="fb"