from django.db import models


class Project(models.Model):
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)


class Organisation(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    alternate_name = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    tax_status = models.TextField(null=True, blank=True)
    tax_id = models.TextField(null=True, blank=True)
    tax_id = models.TextField(null=True, blank=True)
    year_incorporated = models.PositiveIntegerField(null=True, blank=True)
    legal_status = models.TextField(null=True, blank=True)


class Program(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    alternate_name = models.TextField(null=True, blank=True)


class Service(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)
    alternate_name = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    interpretation_services = models.TextField(null=True, blank=True)
    application_process = models.TextField(null=True, blank=True)
    wait_time = models.TextField(null=True, blank=True)
    fees = models.TextField(null=True, blank=True)
    accreditations = models.TextField(null=True, blank=True)
    licenses = models.TextField(null=True, blank=True)


class Taxonomy(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    vocabulary = models.TextField(null=True, blank=True)


class ServiceTaxonomy(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    taxonomy = models.ForeignKey(Taxonomy, on_delete=models.CASCADE, null=True, blank=True)
    taxonomy_detail =  models.TextField(null=True, blank=True)


class Location(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)
    alternate_name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    organization = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True, blank=True)
    transportation = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


class ServiceAtLocation(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)



class Contact(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    service_at_location = models.ForeignKey(ServiceAtLocation, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    department = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)



class Phone(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    organization = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True)
    service_at_location_id = models.ForeignKey(ServiceAtLocation, on_delete=models.CASCADE, null=True, blank=True)
    number = models.TextField(null=True, blank=True)
    extension = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    language = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)



class PhysicalAddress(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    attention = models.TextField(null=True, blank=True)
    address_1 = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    region = models.TextField(null=True, blank=True)
    state_province = models.TextField(null=True, blank=True)
    postal_code = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)

class PostalAddress(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    attention = models.TextField(null=True, blank=True)
    address_1 = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    region = models.TextField(null=True, blank=True)
    state_province = models.TextField(null=True, blank=True)
    postal_code = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)

class RegularSchedule(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    service_at_location = models.ForeignKey(ServiceAtLocation, on_delete=models.CASCADE, null=True, blank=True)
    weekday = models.PositiveIntegerField(null=True, blank=True)  ##### WHAT NUMBER MEANS WHAT ????
    opens_at = models.TextField(null=True, blank=True)
    closes_at = models.TextField(null=True, blank=True)


class HolidaySchedule(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    service_at_location = models.ForeignKey(ServiceAtLocation, on_delete=models.CASCADE, null=True, blank=True)
    closed = models.BooleanField(null=True, blank=True)
    opens_at = models.TextField(null=True, blank=True)
    closes_at = models.TextField(null=True, blank=True)
    start_date = models.TextField(null=True, blank=True)
    end_date = models.TextField(null=True, blank=True)


class Funding(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    source = models.TextField(null=True, blank=True)


class Eligibility(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    eligibility = models.TextField(null=True, blank=True)


class ServiceArea(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    service_area = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class RequiredDocument(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    document = models.TextField(null=True, blank=True)


class PaymentAccepted(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    payment = models.TextField(null=True, blank=True)


class Language(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    language = models.TextField(null=True, blank=True)


class AccessibilityForDisabilities(models.Model):
    standard_id = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    accessibility = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)

