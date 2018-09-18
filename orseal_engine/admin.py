from django.contrib import admin

from .models import *

admin.site.register(Project)
admin.site.register(DataOrganization)
admin.site.register(DataProgram)
admin.site.register(DataService)
admin.site.register(DataTaxonomy)
admin.site.register(DataServiceTaxonomy)
admin.site.register(DataLocation)
admin.site.register(DataServiceAtLocation)
admin.site.register(DataContact)
admin.site.register(DataPhone)
admin.site.register(DataPhysicalAddress)
admin.site.register(DataPostalAddress)
admin.site.register(DataRegularSchedule)
admin.site.register(DataHolidaySchedule)
admin.site.register(DataFunding)
admin.site.register(DataEligibility)
admin.site.register(DataServiceArea)
admin.site.register(DataRequiredDocument)
admin.site.register(DataPaymentAccepted)
admin.site.register(DataLanguage)
admin.site.register(DataAccessibilityForDisabilities)
