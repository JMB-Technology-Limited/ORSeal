from django.db import models
from django.contrib.postgres.fields import JSONField

class Project(models.Model):
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)


class DataOrganisation(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    alternate_name = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    tax_status = models.TextField(null=True, blank=True)
    tax_id = models.TextField(null=True, blank=True)
    year_incorporated = models.PositiveIntegerField(null=True, blank=True)
    legal_status = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataProgram(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    organization = models.ForeignKey(DataOrganisation, on_delete=models.PROTECT, null=True, blank=True)
    organization_data_id = models.UUIDField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    alternate_name = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataService(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    program = models.ForeignKey(DataProgram, on_delete=models.PROTECT, null=True, blank=True)
    program_data_id = models.UUIDField(null=True, blank=True)
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
    other_data = JSONField(null=True, blank=True)


class DataTaxonomy(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    name = models.TextField(null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    parent_data_id = models.UUIDField(null=True, blank=True)
    parent_name = models.TextField(null=True, blank=True)
    vocabulary = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataServiceTaxonomy(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    taxonomy = models.ForeignKey(DataTaxonomy, on_delete=models.PROTECT, null=True, blank=True)
    taxonomy_data_id = models.UUIDField(null=True, blank=True)
    taxonomy_detail =  models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataLocation(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    name = models.TextField(null=True, blank=True)
    alternate_name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    organization = models.ForeignKey(DataOrganisation, on_delete=models.PROTECT, null=True, blank=True)
    organization_data_id = models.UUIDField(null=True, blank=True)
    transportation = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataServiceAtLocation(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    location = models.ForeignKey(DataLocation, on_delete=models.PROTECT, null=True, blank=True)
    location_data_id = models.UUIDField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)



class DataContact(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    organization = models.ForeignKey(DataOrganisation, on_delete=models.PROTECT, null=True, blank=True)
    organization_data_id = models.UUIDField(null=True, blank=True)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    service_at_location = models.ForeignKey(DataServiceAtLocation, on_delete=models.PROTECT, null=True, blank=True)
    service_at_location_data_id = models.UUIDField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    department = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)



class DataPhone(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    location = models.ForeignKey(DataLocation, on_delete=models.PROTECT, null=True, blank=True)
    location_data_id = models.UUIDField(null=True, blank=True)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    organization = models.ForeignKey(DataOrganisation, on_delete=models.PROTECT, null=True, blank=True)
    organization_data_id = models.UUIDField(null=True, blank=True)
    contact = models.ForeignKey(DataContact, on_delete=models.PROTECT, null=True, blank=True)
    contact_data_id = models.UUIDField(null=True, blank=True)
    service_at_location = models.ForeignKey(DataServiceAtLocation, on_delete=models.PROTECT, null=True, blank=True)
    service_at_location_data_id = models.UUIDField(null=True, blank=True)
    number = models.TextField(null=True, blank=True)
    extension = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    language = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataPhysicalAddress(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    location = models.ForeignKey(DataLocation, on_delete=models.PROTECT, null=True, blank=True)
    location_data_id = models.UUIDField(null=True, blank=True)
    attention = models.TextField(null=True, blank=True)
    address_1 = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    region = models.TextField(null=True, blank=True)
    state_province = models.TextField(null=True, blank=True)
    postal_code = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)

class DataPostalAddress(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    location = models.ForeignKey(DataLocation, on_delete=models.PROTECT, null=True, blank=True)
    location_data_id = models.UUIDField(null=True, blank=True)
    attention = models.TextField(null=True, blank=True)
    address_1 = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    region = models.TextField(null=True, blank=True)
    state_province = models.TextField(null=True, blank=True)
    postal_code = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)

class DataRegularSchedule(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    location = models.ForeignKey(DataLocation, on_delete=models.PROTECT, null=True, blank=True)
    location_data_id = models.UUIDField(null=True, blank=True)
    service_at_location = models.ForeignKey(DataServiceAtLocation, on_delete=models.PROTECT, null=True, blank=True)
    service_at_location_data_id = models.UUIDField(null=True, blank=True)
    weekday = models.PositiveIntegerField(null=True, blank=True)  ##### WHAT NUMBER MEANS WHAT ????
    opens_at = models.TextField(null=True, blank=True)
    closes_at = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataHolidaySchedule(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    location = models.ForeignKey(DataLocation, on_delete=models.PROTECT, null=True, blank=True)
    location_data_id = models.UUIDField(null=True, blank=True)
    service_at_location = models.ForeignKey(DataServiceAtLocation, on_delete=models.PROTECT, null=True, blank=True)
    service_at_location_data_id = models.UUIDField(null=True, blank=True)
    closed = models.BooleanField(null=True, blank=True)
    opens_at = models.TextField(null=True, blank=True)
    closes_at = models.TextField(null=True, blank=True)
    start_date = models.TextField(null=True, blank=True)
    end_date = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataFunding(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    organization = models.ForeignKey(DataOrganisation, on_delete=models.PROTECT, null=True, blank=True)
    organization_data_id = models.UUIDField(null=True, blank=True)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    source = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataEligibility(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    eligibility = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataServiceArea(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    service_area = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataRequiredDocument(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    document = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataPaymentAccepted(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    payment = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataLanguage(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    service = models.ForeignKey(DataService, on_delete=models.PROTECT, null=True, blank=True)
    service_data_id = models.UUIDField(null=True, blank=True)
    location = models.ForeignKey(DataLocation, on_delete=models.PROTECT, null=True, blank=True)
    location_data_id = models.UUIDField(null=True, blank=True)
    language = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)


class DataAccessibilityForDisabilities(models.Model):
    data_id = models.UUIDField(null=True, blank=True, unique=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    location = models.ForeignKey(DataLocation, on_delete=models.PROTECT, null=True, blank=True)
    location_data_id = models.UUIDField(null=True, blank=True)
    accessibility = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    other_data = JSONField(null=True, blank=True)

