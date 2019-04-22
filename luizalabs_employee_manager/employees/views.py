from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeList(generics.ListCreateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveDestroyAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def delete(self, request, pk):
        # Delete object with this pk
        employee = get_object_or_404(self.get_queryset(), pk=pk)
        employee.delete()
        return Response({"message": "success"},status=status.HTTP_202_ACCEPTED)
        