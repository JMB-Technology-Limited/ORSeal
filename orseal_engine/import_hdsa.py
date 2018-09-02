from .models import *
import datetime
import requests

class ImportHSDA:

    def go(self):

        now = datetime.datetime.now()
        project = Project()
        project.title = "Import HSDA {}".format(now.strftime("%Y-%m-%d-%H-%M-%S"))
        project.slug = "import_hsda_{}".format(now.strftime("%Y-%m-%d-%H-%M-%S"))
        project.save()

        r = requests.get('http://miami.open.211.hsda.api.adopta.agency/organizations/full/?page=1&per_page=10')
        if r.status_code != 200:
            raise Exception("Got {}".format(r.status_code));

        for data in r.json():

            organization = DataOrganization()
            organization.project = project
            organization.data_id = data["id"]
            organization.name = data["name"]
            organization.alternate_name = data["alternate_name"]
            organization.description = data["description"]
            organization.email = data["email"]
            organization.url = data["url"]
            organization.tax_status = data["tax_status"]
            organization.tax_id = data["tax_id"]
            organization.year_incorporated = data["year_incorporated"]
            organization.legal_status = data["legal_status"]
            organization.save()

