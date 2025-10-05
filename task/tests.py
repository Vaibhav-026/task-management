from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import TaskApplicationUser as User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import TaskDetails

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

class TaskManagerTests(APITestCase):

    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin", password="adminpass", is_admin=True
        )
        self.regular_user = User.objects.create_user(
            username="user", password="userpass"
        )

        self.task = TaskDetails.objects.create(
            title="Test Task", description="Desc", completed=False
        )

        self.list_url = reverse("task-manager")
        self.detail_url = reverse("task-details", args=[self.task.id])

    def test_admin_can_delete_task(self):
        token = get_token_for_user(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_regular_user_cannot_delete_task(self):
        token = get_token_for_user(self.regular_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_user_cannot_delete_task(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_tasks_authenticated(self):
        token = get_token_for_user(self.regular_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task_authenticated(self):
        token = get_token_for_user(self.regular_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        data = {"title": "New Task", "description": "Created in test"}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
