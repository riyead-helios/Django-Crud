from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from django.http.response import JsonResponse
from django.http.response import Http404
from rest_framework.response import Response

from .models import Employee


class EmployeeView(APIView):

    def get_employee(self, pk):
        try:
            employee = Employee.objects.get(employeeId=pk)
            return employee
        except: 
            return JsonResponse("Employee Does Not Exist")
        
    def get(self, request, pk=None):
        if pk:
            data = self.get_employee(pk)
            serializer = EmployeeSerializer(data)
        else:
            data = Employee.objects.all()
            serializer = EmployeeSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = EmployeeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse("Failed to Add Employee", safe=False)
    
    def put(self, request, pk=None):
        employee_to_update = Employee.objects.get(employeeId=pk)
        serializer = EmployeeSerializer(instance=employee_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Employee Updated Successfully", safe=False)
        return JsonResponse("Faild to Update Employee")
    
    def delete(self, request, pk=None):
        employee_to_delete = Employee.objects.get(employeeId= pk)
        employee_to_delete.delete()
        return JsonResponse("Employee Deleted Successfully", safe=False)