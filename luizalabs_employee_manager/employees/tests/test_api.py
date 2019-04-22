import pytest, requests, json
from rest_framework import status
from django.urls import reverse
from django.test import Client
from ..models import Employee

client = Client()

@pytest.mark.django_db
class TestEmployeeViews:

    def setup(self):

        self.arnaldo = Employee.objects.create(name='Arnaldo Pereira', email='arnaldo@luizalabs.com', department='Architecture')
        self.renato = Employee.objects.create(name='Renato Pedigoni', email='renato@luizalabs.com', department='E-commerce')
        self.thiago = Employee.objects.create(name='Thiago Catoto', email='catoto@luizalabs.com', department='Mobile')

    def test__list_employees(self):
        
        response = client.get(reverse('employee:list-create'))
        response_json = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_json[0]['name'] == self.arnaldo.name

    def test__add_employees(self):
        
        data = {
            'name': 'Teste API',
            'email': 'teste@luizalabs.com',
            'department': 'Teste Departamento'
        }

        response = client.post(
            reverse('employee:list-create'), 
            data=json.dumps(data),
            content_type='application/json'
        )

        assert response.status_code == status.HTTP_201_CREATED

    def test__delete_employees(self):

        response = client.delete(reverse('employee:delete', args=[self.arnaldo.pk]))

        assert response.status_code == status.HTTP_202_ACCEPTED