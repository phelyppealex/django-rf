from rest_framework.response import Response
from rest_framework.decorators import api_view
from app_base.models import Employee
from .serializers import EmployeeSerializer

@api_view(['GET'])
def getData(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addEmployee(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
