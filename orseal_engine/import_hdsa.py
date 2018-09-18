from .models import *
import datetime
import requests

class ImportHSDA:

    def __init__(self):
        self.results_per_page = 10

    def go(self):

        now = datetime.datetime.now()
        self.project = Project()
        self.project.title = "Import HSDA {}".format(now.strftime("%Y-%m-%d-%H-%M-%S"))
        self.project.slug = "import_hsda_{}".format(now.strftime("%Y-%m-%d-%H-%M-%S"))
        self.project.save()

        self._import_organisations()
        self._import_services()

    def _import_organisations(self):

        page = 1
        continue_to_process = True

        while continue_to_process:

            url = 'http://miami.open.211.hsda.api.adopta.agency/organizations/?page={}&per_page={}'.format(page, self.results_per_page)
            print(url)
            r = requests.get(url)
            if r.status_code != 200:
                raise Exception("Got {}".format(r.status_code))

            continue_to_process = False

            for data in r.json():

                continue_to_process = True

                try:
                    organization = DataOrganization.objects.get(project=self.project, data_id=data["id"])
                except DataOrganization.DoesNotExist:
                    organization = DataOrganization()
                    organization.project = self.project
                    organization.data_id = data["id"]

                if data["name"]:
                    organization.name = data["name"]
                if data["alternate_name"]:
                    organization.alternate_name = data["alternate_name"]
                if data["description"]:
                    organization.description = data["description"]
                if data["email"]:
                    organization.email = data["email"]
                if data["url"]:
                    organization.url = data["url"]
                if data["tax_status"]:
                    organization.tax_status = data["tax_status"]
                if data["tax_id"]:
                    organization.tax_id = data["tax_id"]
                if data["year_incorporated"]:
                    organization.year_incorporated = data["year_incorporated"]
                if data["legal_status"]:
                    organization.legal_status = data["legal_status"]
                organization.save()

            page += 1

    def _import_services(self):

        page = 1
        continue_to_process = True

        while continue_to_process:

            url = 'http://miami.open.211.hsda.api.adopta.agency/services/?page={}&per_page={}'.format(page, self.results_per_page)

            print(url)
            r = requests.get(url)
            if r.status_code != 200:
                raise Exception("Got {}".format(r.status_code))

            continue_to_process = False

            for data in r.json():

                continue_to_process = True

                try:
                    service = DataService.objects.get(project=self.project, data_id=data["id"])
                except DataService.DoesNotExist:
                    service = DataService()
                    service.project = self.project
                    service.data_id = data["id"]

                if data["name"]:
                    service.name = data["name"]
                if data["description"]:
                    service.description = data["description"]
                if data["program_id"]:
                    service.program_data_id = data["program_id"]
                if data["alternate_name"]:
                    service.alternate_name = data["alternate_name"]
                if data["email"]:
                    service.email = data["email"]
                if data["url"]:
                    service.url = data["url"]
                if data["status"]:
                    service.status = data["status"]
                if data["interpretation_services"]:
                    service.interpretation_services = data["interpretation_services"]
                if data["application_process"]:
                    service.application_process = data["application_process"]
                if data["wait_time"]:
                    service.wait_time = data["wait_time"]
                if data["fees"]:
                    service.fees = data["fees"]
                if data["accreditations"]:
                    service.accreditations = data["accreditations"]
                if data["licenses"]:
                    service.licenses = data["licenses"]
                service.save()

            page += 1
