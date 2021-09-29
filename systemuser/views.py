from django.http.response import JsonResponse
from systemuser.forms import EmployeeForm
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Employee, EvotingUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from election.models import Voter
from django.conf import settings
User = settings.AUTH_USER_MODEL





# Create your views here.






# view (controler) methods for voters starts here

def index(request):
    return render(request,'systemuser/index.html')

def index1(request):
    return render(request, 'systemuser/index1.html')


def voter_login(request):
    # current_user = None;
    error_message = "Invalid VRID and/or Password"
    if request.method =='POST':
        vrid = request.POST['VRID']
        password = request.POST['password']
        voter = Voter.objects.all().filter(voter_registration_id=vrid, voter_password=password)
        print(voter)
        if len(voter) > 0:
            current_user = voter;
            return render(request, 'voter_index.html', {'current_user': current_user})
        else:
            return render(request, 'systemuser/voter_login.html', {'error_message': error_message})
            

    return render(request, 'systemuser/voter_login.html')

def login_process(request):
    
    if request.method =='POST':
       
        context = {} 
        # if form.errors:
        #     return render(request, 'systemuser/login.html', context)    
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view_voter')
        
        else:
            # return HttpResponse("You are not an authorized user")
            messages.info(request, 'Invalid Username and/or Password ')
            return render(request, 'systemuser/login.html', {'messags':messages}) 
    else:
        return render(request, 'systemuser/login.html')

def logout_process(request):
    logout(request)
    return redirect('login')




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
        employee_data = EvotingUser.objects.all()
        return render(request, 'systemuser/view_employee.html', {'var':'v', 'employee_data':employee_data})
    
    elif request.method == 'POST':
        employee_data = EvotingUser.objects.all().filter(first_name=request.POST.get('search'))
        return render(request, 'systemuser/view_employee.html', {'var':'v', 'employee_data':employee_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'systemuser/view_employee.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'systemuser/view_employee.html', {'var':'v'})

@login_required()
def update_employee(request, id):
    if request.method == 'GET':
        employee_instance = EvotingUser.objects.get(pk=id)
        form = EmployeeForm(instance=employee_instance)
        return render(request, 'systemuser/update_employee.html',{'var':'v', 'form': form})

    else:
        employee_instance = EvotingUser.objects.get(pk=id)
        form = EmployeeForm(request.POST, request.FILES, instance= employee_instance)
        if form.is_valid():
            form.save()
        return redirect('view_employee')



def delete_employee(request, id):
    employee_instance = EvotingUser.objects.get(pk=id)
    employee_instance.delete()
    return redirect('view_employee')




# view (controler) methods for employees starts here





