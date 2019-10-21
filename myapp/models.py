from django.db import models

# Create your models here.
class Register(models.Model):
	Name=models.CharField(max_length=25)
	Email=models.CharField(max_length=25)
	Mobile_no=models.CharField(max_length=10)
	Course=models.CharField(max_length=25)
	Source=models.CharField(max_length=25)
	Lead_status = models.CharField(max_length=20)
	Demo_date = models.CharField(max_length = 20)
	Counsler = models.CharField(max_length=20)
	Remark = models.CharField(max_length = 20)


	def __str__(self):
		return self.Name

class Join(models.Model):
	name = models.CharField(max_length=25)
	Course = models.CharField(max_length=25)
	DOJ = models.CharField(max_length=25)
	DOC = models.CharField(max_length=25)
	Course_fee = models.CharField(max_length=25)
	Instructor = models.CharField(max_length=25)
	Aadhar = models.CharField(max_length=25)
	mobile = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	remark = models.CharField(max_length=25)
	status=models.CharField(max_length=25)

	def __str__(self):
		return self.name

