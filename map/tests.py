from django.test import TestCase
from map.models import Poi
from django.shortcuts import reverse
class PoiTestCase(TestCase):
    def creatingTest(self):
        Poi.objects.create(lat="71.50066", lon="30.174174", category="verygood", is_active=True)

    def gettingTest(self):
        Poi.objects.create(lat="71.50066", lon="30.174174", category="verygood", is_active=True)
        lion = Poi.objects.get(is_active=True, lat = "71.50066")
    def testView(self):
        resp = self.client.get('/')

        self.assertEqual(resp.status_code, 200)