from django.db import models

class Overview(models.Model):
    overview = models.CharField(max_length=2000)

class Skill(models.Model):
    skills=models.CharField(max_length=400)

class Image(models.Model):
    images=models.URLField(max_length=2000)

class Sample(models.Model):
    frontEnd=models.CharField(max_length=3000)
    backEnd=models.CharField(max_length=3000)

class Language(models.Model):
    languages = models.CharField(max_length=255)

class Framework(models.Model):
    frameworks = models.CharField(max_length=800)

class Target(models.Model):
    Targets = models.CharField(max_length=1000)


