"""Tests for department and machine list views."""

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from .models import Department, Machine


class DepartmentMachineViewTests(TestCase):
    def setUp(self) -> None:
        User = get_user_model()
        self.manager = User.objects.create_user(
            username="manager", password="pass", role="manager"
        )
        self.worker = User.objects.create_user(
            username="worker", password="pass", role="worker"
        )
        self.department = Department.objects.create(name="Assembly")
        self.machine = Machine.objects.create(
            name="Lathe", serial_number="SN123", department=self.department
        )

    def test_worker_only_sees_lists(self):
        self.client.login(username="worker", password="pass")
        dept_response = self.client.get(reverse("department_list"))
        self.assertContains(dept_response, "Assembly")
        self.assertNotContains(dept_response, "Add Department")
        self.assertNotContains(
            dept_response, reverse("delete_department", args=[self.department.id])
        )

        machine_response = self.client.get(reverse("machine_list"))
        self.assertContains(machine_response, "Lathe")
        self.assertNotContains(machine_response, "Add Machine")
        self.assertNotContains(
            machine_response, reverse("delete_machine", args=[self.machine.id])
        )

    def test_manager_sees_forms_and_delete_buttons(self):
        self.client.login(username="manager", password="pass")
        dept_response = self.client.get(reverse("department_list"))
        self.assertContains(dept_response, "Add Department")
        self.assertContains(
            dept_response, reverse("delete_department", args=[self.department.id])
        )

        machine_response = self.client.get(reverse("machine_list"))
        self.assertContains(machine_response, "Add Machine")
        self.assertContains(
            machine_response, reverse("delete_machine", args=[self.machine.id])
        )

    def test_manager_can_delete(self):
        self.client.login(username="manager", password="pass")
        self.client.post(reverse("delete_machine", args=[self.machine.id]))
        self.assertFalse(Machine.objects.filter(id=self.machine.id).exists())
        self.client.post(reverse("delete_department", args=[self.department.id]))
        self.assertFalse(Department.objects.filter(id=self.department.id).exists())

    def test_worker_cannot_delete(self):
        self.client.login(username="worker", password="pass")
        self.client.post(reverse("delete_machine", args=[self.machine.id]))
        self.client.post(reverse("delete_department", args=[self.department.id]))
        self.assertTrue(Machine.objects.filter(id=self.machine.id).exists())
        self.assertTrue(Department.objects.filter(id=self.department.id).exists())

