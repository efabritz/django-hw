from rest_framework.test import APITestCase

class TestLogistic(APITestCase):
    def test_mult(self):
        self.assertEqual('ddd', 'd' * 3)