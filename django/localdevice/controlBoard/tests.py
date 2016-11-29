import os

from django.test import TestCase

from controlBoard.api import views


class ControlBoardTestCase(TestCase):
    def setUp(self):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'localdevice.settings'
        pass

    def test_api_rotate(self):
        views.rotate(1)

