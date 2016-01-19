from django.test import TestCase
from models import *
import factory
from apps.companies.models import *
from django.test.client import Client
from apps.users.tests import UserFactory
from apps.companies.tests import CompaniesFactory

class CampaignFactory(factory.Factory):
    class Meta:
        model = Campaign

    name = "SampleSite"
    description = "Some words about campaign "


class CampaignTests(TestCase):
    c = Client()
    
    campaign = CampaignFactory()
    rawName = "SampleSite"
    rawDesc = "Some words about campaign "
    

    def test_name(self):
        name = self.campaign.name
        self.assertEqual(name, self.rawName, "Campaign test_name Failed")
        print "Campaign test_name Passed"

    def test_desc(self):
        desc = self.campaign.description
        self.assertEqual(desc, self.rawDesc, "Campaign test_desc Failed")
        print "Campaign test_desc Passed"

    def test_save(self):
        #TODO: should not be able to create campaign without a company
        register = self.c.post('/users/auth/register/', {'name' : 'SampleName', 'email' : 'selftest@example.com', 'password1' : 'alphanum', 'password2' : 'alphanum'})
        company = Company.objects.get(name='SampleName')
        response = self.campaign.save()
        check = Campaign.objects.get(name="SampleSite")
        self.assertEqual(check.name, "SampleSite", "Campaign test_save Failed")
        self.assertEqual(check.description, self.rawDesc, "Campaign test_save Failed")
        
        print "Campaign test_save Passed"
        
        #invoice = self.campaign.set_invoice(self)

        """
    def test_set_invoice(self):
        
        Still not figured out 

        """
        
        
