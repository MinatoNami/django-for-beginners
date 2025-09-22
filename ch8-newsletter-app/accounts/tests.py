from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(reverse("signup"), {
            "username": "testuser",
            "email": "testuser@example.com",
            "age": 25,
            "password1": "complexpassword123",
            "password2": "complexpassword123",
        })
        # Redirect after successful signup
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.first().username, "testuser")
        self.assertEqual(get_user_model().objects.first().email,
                         "testuser@example.com")
        self.assertEqual(get_user_model().objects.first().age, 25)
