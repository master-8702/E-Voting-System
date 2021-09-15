from django.http.response import JsonResponse
from systemuser.forms import EmployeeForm, VoterForm
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import VoterForm
from .models import Employee, Voter, EvotingUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse





# Create your views here.

def view_live_voters_counter(request):
    # data = len(EvotingUser.objects.all())

    return render(request,'election/view_live_voters_counter.html')

def fetch_voter_data(request):
    data = len(EvotingUser.objects.all())
    # data2 = EvotingUser.objects.all()


    # return JsonResponse({"data":list(data2.values())})
    return JsonResponse({'data':data})






# view (controler) methods for voters starts here

def index(request):
    return render(request,'systemuser/index.html')

def index1(request):
    return render(request, 'systemuser/index1.html')

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


@login_required(login_url='login')
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
        return render(request, 'systemuser/view_voter.html', {'var':'v', 'voter_data':voter_data, 'request':request})
    
    elif request.method == 'POST':
        voter_data = Voter.objects.all().filter(first_name=request.POST.get('search'))
        return render(request, 'systemuser/view_voter.html', {'var':'v', 'voter_data':voter_data, 'user':request.user})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'systemuser/view_voter.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'systemuser/view_voter.html', {'var':'v'})

@login_required()
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





