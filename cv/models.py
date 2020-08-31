from django.db import models

class CV(models.Model):
	full_name = models.CharField(max_length=200, default='', blank=True)
	email = models.CharField(max_length=200, default='', blank=True)
	website = models.CharField(max_length=200, default='', blank=True)
	mobile_number = models.CharField(max_length=200, default='', blank=True)
	job_title = models.CharField(max_length=200, default='', blank=True)
	personal_profile = models.TextField(default='', blank=True)
	key_skills = models.TextField(default='', blank=True)

	def __str__(self):
		return self.full_name

class Education(models.Model):
	cv = models.ForeignKey(CV, on_delete=models.CASCADE)
	institution = models.CharField(max_length=100)
	qualification = models.CharField(max_length=100)
	description = models.TextField(max_length=100)

	def __str__(self):
		return self.qualification

class WorkExperience(models.Model):
	cv = models.ForeignKey(CV, on_delete=models.CASCADE)
	job_title = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	from_date = models.DateTimeField(blank=True, null=True)
	to_date = models.DateTimeField(blank=True, null=True) # a null to_date should be interpreted as 'Present'
	description = models.TextField(max_length=100)
	
	def __str__(self):
		return self.description