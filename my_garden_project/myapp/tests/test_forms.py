from django.test import TestCase
from ..forms import *
from ..models import *


class TestForms(TestCase):

    def test_create_user_form(self):
        print("creation user")
        form = CreateUserForm(data={'username': 'user_test', 'email': 'user_test@test.com', 'password1': 'UserTestPwd123',
                                    'password2': 'UserTestPwd123'})
        self.assertTrue(form.is_valid(), form.errors)





