from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def about(request):
    #return render(request, 'index.html', {})
    return render(request, 'about.html')

def department(request):
    items = models.Department.objects.all()
    return render(request, 'department.html', {'items': items})

def employee(request):
    items = models.Employee.objects.all()
    return render(request, 'employee.html', {'items': items})


"""
{% block table %}
<table>
{% for item in items %}
<tr>
    <td>{{item.name}}</td>
</tr>
</table>
{% endblock %}
"""