from django.db import models

# Create your models here.

class ITjobs(models.Model):
    company_name         = models.CharField(max_length=70)
    year_of_experience   = models.IntegerField()
    job_description      = models.TextField()
    job_role             = models.CharField(max_length=80)
    location             = models.CharField(max_length=80)
    package              = models.FloatField()


    def __str__(self):
        return self.company_name


class MECHjobs(models.Model):
    company_name         = models.CharField(max_length=70)
    year_of_experience   = models.IntegerField()
    job_description      = models.TextField()
    job_role             = models.CharField(max_length=80)
    location             = models.CharField(max_length=80)
    package              = models.FloatField()


    def __str__(self):
        return self.company_name


class CIVILjobs(models.Model):
    company_name         = models.CharField(max_length=70)
    year_of_experience   = models.IntegerField()
    job_description      = models.TextField()
    job_role             = models.CharField(max_length=80)
    location             = models.CharField(max_length=80)
    package              = models.FloatField()


    def __str__(self):
        return self.company_name


class ImageTable(models.Model):
    image       = models.ImageField(upload_to = "pics")
    discription = models.TextField()
