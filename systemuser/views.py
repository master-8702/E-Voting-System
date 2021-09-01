from systemuser.forms import VoterForm
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import VoterForm
from .models import Voter


# Create your views here.

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
        if form.is_valid():
            form.save()
        return redirect('register_voter')




def view_voter(request):
    if request.method == 'POST' and request.POST.get('search') == '__all__':
            voter_data = Voter.objects.all()
            return render(request, 'systemuser/view_voter.html', {'var':'v', 'voter_data':voter_data})
    
    elif request.method == 'POST':
        voter_data = Voter.objects.all().filter(voter_name=request.POST.get('search'))
        return render(request, 'systemuser/view_voter.html', {'var':'v', 'voter_data':voter_data})

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
