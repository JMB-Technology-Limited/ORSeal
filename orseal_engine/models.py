from django.db import models


class Project(models.Model):
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)


class Organisation(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()


class Program(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()


class Service(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()


class ServiceTaxonomy(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ServiceAtLocation(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Location(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()


class Phone(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Contact(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class PhysicalAddress(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class PostalAddress(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class RegularScheduleAddress(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class HolidayScheduleAddress(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Funding(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Eligibility(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ServiceArea(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class RequiredDocument(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class PaymentAccepted(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class PaymentAccepted(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Language(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class AccessibilityForDisabilities(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Taxonomy(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

