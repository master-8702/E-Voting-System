from systemuser.forms import VoterForm
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ElectionForm, PartyForm
from .models import Election, Party


# Create your views here.

# view (controler) methods for parties starts here


def register_party(request):
    if request.method == 'GET':
        form = PartyForm()
        return render(request, 'election/create_party.html', {'form': form, 'var':'r'})

    else:
        form = PartyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'election/create_party.html', {'form': form, 'var':'r'})
        return redirect('register_party')




def view_party(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        party_data = Party.objects.all()
        print(party_data[0].part_logo.url) 
        return render(request, 'election/view_party.html', {'var':'v', 'party_data':party_data})
    
    elif request.method == 'POST':
        party_data = Party.objects.all().filter(party_name__iexact=request.POST.get('search'))
        return render(request, 'election/view_party.html', {'var':'v', 'party_data':party_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'election/view_party.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'election/view_party.html', {'var':'v'})

def update_party(request, id):
    if request.method == 'GET':
        party_instance = Party.objects.get(pk=id)
        form = PartyForm(instance=party_instance)
        return render(request, 'election/update_party.html',{'var':'v', 'form': form})

    else:
        # here we have to add request.FILES in order to receive file uploads like images 
        party_instance = Party.objects.get(pk=id)
        form = PartyForm(request.POST, request.FILES, instance= party_instance)
        if form.is_valid():
            form.save()
        return redirect('view_party')





def delete_party(request, id):
    party_instance = Party.objects.get(pk=id)
    party_instance.delete()
    return redirect('view_party')


# view (controler) methods for parties ends here



# view (controler) methods for Election starts here


def register_election(request):
    if request.method == 'GET':
        form = ElectionForm()
        return render(request, 'election/create_election.html', {'form': form, 'var':'r'})

    else:
        form = ElectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'election/create_election.html', {'form': form, 'var':'r'})
        return redirect('register_election')




def view_election(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        election_data = Election.objects.all()
        return render(request, 'election/view_election.html', {'var':'v', 'election_data':election_data})
    
    elif request.method == 'POST' and not (request.POST.get('search') ==''):
        election_data = Election.objects.all().filter(election_name__icontains=request.POST.get('search'))
        return render(request, 'election/view_election.html', {'var':'v', 'election_data':election_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'election/view_election.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'election/view_election.html', {'var':'v'})

def update_election(request, id):
    if request.method == 'GET':
        election_instance = Election.objects.get(pk=id)
        form = ElectionForm(instance=election_instance)
        return render(request, 'election/update_election.html',{'var':'v', 'form': form})

    else:
        election_instance = Election.objects.get(pk=id)
        form = ElectionForm(request.POST, instance= election_instance)
        if form.is_valid():
            form.save()
        return redirect('view_election')





def delete_election(request, id):
    election_instance = Election.objects.get(pk=id)
    election_instance.delete()
    return redirect('view_election')



# view (controler) methods for Election ends here




