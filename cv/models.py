from django.db import models

class ContactInformation(models.Model):
    name = models.CharField(max_length=100, default='SATYA DEEP DASARI')
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    professional_summary = models.TextField()

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    cgpa = models.FloatField()

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.TextField()  # This can be JSON or another structured format for multiple bullet points

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)  # e.g., Beginner, Intermediate, Expert

class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)

class ResearchExperience(models.Model):
    topic = models.CharField(max_length=200)
    conference = models.CharField(max_length=200)
    publication = models.CharField(max_length=200)

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class VolunteerExperience(models.Model):
    role = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    description = models.TextField()

class Award(models.Model):
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)

class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()

