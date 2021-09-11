from systemuser.forms import EmployeeForm, VoterForm
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import VoterForm
from .models import Employee, Voter


# Create your views here.

# view (controler) methods for voters starts here

def index(request):
    return render(request,'systemuser/index.html')

def index1(request):
    return render(request, 'systemuser/index1.html')

def register_voter(request):
    if request.method == 'GET':
        form = VoterForm()
        return render(request, 'systemuser/create_voter.html', {'form': form, 'var':'r'})

    else:
        form = VoterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(request.POST)
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'systemuser/create_voter.html', {'form': form, 'var':'r'})
        return redirect('register_voter')




def view_voter(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        voter_data = Voter.objects.all()
        return render(request, 'systemuser/view_voter.html', {'var':'v', 'voter_data':voter_data})
    
    elif request.method == 'POST':
        voter_data = Voter.objects.all().filter(first_name=request.POST.get('search'))
        return render(request, 'systemuser/view_voter.html', {'var':'v', 'voter_data':voter_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'systemuser/view_voter.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'systemuser/view_voter.html', {'var':'v'})

def update_voter(request, id):
    if request.method == 'GET':
        voter_instance = Voter.objects.get(pk=id)
        form = VoterForm(instance=voter_instance)
        return render(request, 'systemuser/update_voter.html',{'var':'v', 'form': form})

    else:
        voter_instance = Voter.objects.get(pk=id)
        form = VoterForm(request.POST, instance= voter_instance)
        if form.is_valid():
            form.save()
        return redirect('view_voter')



def delete_voter(request, id):
    voter_instance = Voter.objects.get(pk=id)
    voter_instance.delete()
    return redirect('view_voter')


# view (controler) methods for veoters ends here



# view (controler) methods for employees starts here



def register_employee(request):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request, 'systemuser/create_employee.html', {'form': form, 'var':'r'})

    else:
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'systemuser/create_employee.html', {'form': form, 'var':'r'})
        return redirect('register_employee')




def view_employee(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        employee_data = Employee.objects.all()
        return render(request, 'systemuser/view_employee.html', {'var':'v', 'employee_data':employee_data})
    
    elif request.method == 'POST':
        employee_data = Employee.objects.all().filter(first_name=request.POST.get('search'))
        return render(request, 'systemuser/view_employee.html', {'var':'v', 'employee_data':employee_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'systemuser/view_employee.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'systemuser/view_employee.html', {'var':'v'})

def update_employee(request, id):
    if request.method == 'GET':
        employee_instance = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=employee_instance)
        return render(request, 'systemuser/update_employee.html',{'var':'v', 'form': form})

    else:
        employee_instance = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST, request.FILES, instance= employee_instance)
        if form.is_valid():
            form.save()
        return redirect('view_employee')



def delete_employee(request, id):
    employee_instance = Employee.objects.get(pk=id)
    employee_instance.delete()
    return redirect('view_employee')




# view (controler) methods for employees starts here





