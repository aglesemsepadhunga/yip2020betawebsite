from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class extendedteaminfo(models.Model):
	school = models.CharField(max_length=250)
	team_name = models.CharField(max_length=250,unique=True)
	ps = models.IntegerField()
	teacher_name = models.CharField(max_length=200,blank=True)
	teacher_email = models.EmailField(blank=True)
	teacher_phone_num = models.CharField(max_length=12,blank=True)
	num_of_students = models.IntegerField(blank=True,null=True)

	s1_name = models.CharField(blank=True,max_length=200)
	s1_email = models.EmailField()
	s1_phone_num = models.CharField(max_length=12)
	s1_class = models.IntegerField(blank=True,null=True)
	s1_dob = models.DateField(blank=True,null=True)
	s1_gender = models.CharField(max_length=1,default="X")

	s2_name = models.CharField(blank=True,max_length=200)
	s2_email = models.EmailField()
	s2_phone_num = models.CharField(max_length=12)
	s2_class = models.IntegerField(blank=True,null=True)
	s2_dob = models.DateField(blank=True,null=True)
	s2_gender = models.CharField(max_length=1,default="X")

	s3_name = models.CharField(blank=True,max_length=200)
	s3_email = models.EmailField(blank=True)
	s3_phone_num = models.CharField(max_length=12,blank=True)
	s3_class = models.CharField(blank=True,max_length=1)
	s3_dob = models.CharField(blank=True,max_length=10)
	s3_gender = models.CharField(max_length=1,default="X",blank=True)

	user = models.OneToOneField(User,on_delete=models.CASCADE)