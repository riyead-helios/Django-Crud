from django.shortcuts import redirect, render
from multiprocessing import context


from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def Home(request):
    form = EmployeeForm()
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.save()
        form = EmployeeForm()

    # Retrive all Employee and pass it to index.html through context
    data = Employee.objects.all()

    context = {
        'form' : form,
        'data' : data,
    }

    
    return render(request, 'app1/index.html', context)


    

# Update View
def Update_Record(request, id):
    if request.method == 'POST':
        data = Employee.objects.get(pk = id)
        form = EmployeeForm(request.POST, instance = data)
        
        if form.is_valid():
            form.save()

    # Return employee from the Employee model whose primary key matches the id and return single instance/data, then call EmployeeForm class and keep data into instance, then pass form to update.html through context with pre-populated data 
    else:
        data = Employee.objects.get(pk = id)
        form = EmployeeForm(instance = data)

        
    context = {
        'form' : form,
    }

    
    return render (request, 'app1/update.html', context)





# Delete View
def Delete_record(request, id):
    # Return employee from the Employee model whose primary key matches the id
    data = Employee.objects.get(pk = id)
    data.delete()

    
    return redirect('/')
