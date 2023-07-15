from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from todo.models import Task, Tag


class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_login(self.user)
        self.task = Task.objects.create(
            content="Test Task",
            deadline=timezone.now() + timezone.timedelta(days=1),
        )
        self.tag = Tag.objects.create(name="Test Tag")
        self.task.tags.add(self.tag)

    def test_index_view(self):
        response = self.client.get(reverse("todo:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_create_view(self):
        response = self.client.post(
            reverse("todo:task-create"),
            {
                "content": "New Task",
                "deadline": timezone.now() + timezone.timedelta(days=2),
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(content="New Task").exists())

    def test_task_update_view(self):
        response = self.client.post(
            reverse("todo:task-update", kwargs={"pk": self.task.pk}),
            {
                "content": "Task Test Updated",
                "deadline": timezone.now() + timezone.timedelta(days=3),
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(content="Task Test Updated").exists())

    def test_task_delete_view(self):
        url = reverse("todo:task-delete", kwargs={"pk": self.task.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_tag_list_view(self):
        response = self.client.get(reverse("todo:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Tag")

    def test_tag_create_view(self):
        response = self.client.post(reverse("todo:tag-create"), {"name": "New Tag"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())

    def test_tag_update_view(self):
        response = self.client.post(
            reverse("todo:tag-update", kwargs={"pk": self.tag.pk}),
            {
                "name": "Tag updated",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tag.objects.filter(name="Tag updated").exists())

    def test_tag_delete_view(self):
        url = reverse("todo:tag-delete", kwargs={"pk": self.tag.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(name="Test Tag").exists())
