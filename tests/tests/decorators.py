from django.http import HttpResponse
from oauth2_consumer.decorators import scope_required
from .test_cases import DecoratorTestCase
from .mock import TestFunc

class TestDecoratorErrors(DecoratorTestCase):
    def test_test(self):
        response = self.client.get("/no_args/")
        
        print response