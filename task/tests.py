from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskAPITests(APITestCase):
    def setUp(self):
        self.task1 = Task.objects.create(title='Task 1', description='Description 1', due_date='2024-02-14', status='Pending')
        self.task2 = Task.objects.create(title='Task 2', description='Description 2', due_date='2024-02-15', status='In Progress')

    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_task(self):
        url = reverse('task-detail', kwargs={'pk': self.task1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')

    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'New Task', 'description': 'New Description', 'due_date': '2024-02-16', 'status': 'Pending'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)

    def test_update_task(self):
        url = reverse('task-detail', kwargs={'pk': self.task1.pk})
        data = {'title': 'Updated Task', 'description': 'Updated Description', 'due_date': '2024-02-14', 'status': 'Completed'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(pk=self.task1.pk).title, 'Updated Task')

    def test_delete_task(self):
        url = reverse('task-detail', kwargs={'pk': self.task2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)
