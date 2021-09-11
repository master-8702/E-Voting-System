from systemuser.forms import VoterForm
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ObserverForm, ElectionForm, ObserverForm, PartyForm, PollingStationsForm, ReferendumForm, ReferendumOptionsForm, RegionsFrom
RegionsFrom, PollingStationsForm
from .models import Candidates, Election, Observer, Party, Referendum, ReferendumOptions, Regions, PollingStation


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



# view (controler) methods for Referendum starts here


def register_referendum(request):
    if request.method == 'GET':
        form = ReferendumForm()
        return render(request, 'election/create_referendum.html', {'form': form, 'var':'r'})

    else:
        form = ReferendumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'election/create_referendum.html', {'form': form, 'var':'r'})
        return redirect('register_referendum')




def view_referendum(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        candidate_data = Referendum.objects.all()
        return render(request, 'election/view_referendum.html', {'var':'v', 'candidate_data':candidate_data})
    
    elif request.method == 'POST' and not (request.POST.get('search') ==''):
        candidate_data = Referendum.objects.all().filter(referendum_name__icontains=request.POST.get('search'))
        return render(request, 'election/view_referendum.html', {'var':'v', 'candidate_data':candidate_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'election/view_referendum.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'election/view_referendum.html', {'var':'v'})

def update_referendum(request, id):
    if request.method == 'GET':
        referendum_instance = Referendum.objects.get(pk=id)
        form = ReferendumForm(instance=referendum_instance)
        return render(request, 'election/update_referendum.html',{'var':'v', 'form': form})

    else:
        referendum_instance = Referendum.objects.get(pk=id)
        form = ReferendumForm(request.POST, instance= referendum_instance)
        if form.is_valid():
            form.save()
        return redirect('view_referendum')





def delete_referendum(request, id):
    referendum_instance = Referendum.objects.get(pk=id)
    referendum_instance.delete()
    return redirect('view_referendum')



# view (controler) methods for Referendum ends here



# view (controler) methods for Referendum_options starts here


def register_referendum_options(request):
    if request.method == 'GET':
        form = ReferendumOptionsForm()
        return render(request, 'election/create_referendum_options.html', {'form': form, 'var':'r'})

    else:
        form = ReferendumOptionsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'election/create_referendum_options.html', {'form': form, 'var':'r'})
        return redirect('register_referendum_options')




def view_referendum_options(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        referendum_options_data = ReferendumOptions.objects.all()
        return render(request, 'election/view_referendum_options.html', {'var':'v', 'referendum_options_data':referendum_options_data})
    
    elif request.method == 'POST' and not (request.POST.get('search') ==''):
        referendum_options_data = ReferendumOptions.objects.all().filter(referendum_options_name__icontains=request.POST.get('search'))
        return render(request, 'election/view_referendum_options.html', {'var':'v', 'referendum_options_data':referendum_options_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'election/view_referendum_options.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'election/view_referendum_options.html', {'var':'v'})

def update_referendum_options(request, id):
    if request.method == 'GET':
        referendum_options_instance = ReferendumOptions.objects.get(pk=id)
        form = ReferendumOptionsForm(instance=referendum_options_instance)
        return render(request, 'election/update_referendum_options.html',{'var':'v', 'form': form})

    else:
        referendum_options_instance = ReferendumOptions.objects.get(pk=id)
        form = ReferendumOptionsForm(request.POST, instance= referendum_options_instance)
        if form.is_valid():
            form.save()
        return redirect('view_referendum_options')





def delete_referendum_options(request, id):
    referendum_options_instance = ReferendumOptions.objects.get(pk=id)
    referendum_options_instance.delete()
    return redirect('view_referendum_options')



# view (controler) methods for Referendum_options ends here



# view (controler) methods for candidates starts here


def register_candidate(request):
    if request.method == 'GET':
        form = CandidatesForm()
        return render(request, 'election/create_candidate.html', {'form': form, 'var':'r'})

    else:
        form = CandidatesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'election/create_candidate.html', {'form': form, 'var':'r'})
        return redirect('register_candidate')




def view_candidate(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        candidate_data = Candidates.objects.all()
        return render(request, 'election/view_candidate.html', {'var':'v', 'candidate_data':candidate_data})
    
    elif request.method == 'POST' and not (request.POST.get('search') ==''):
        candidate_data = Candidates.objects.all().filter(candidate_name__iexact=request.POST.get('search'))
        return render(request, 'election/view_candidate.html', {'var':'v', 'candidate_data':candidate_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'election/view_candidate.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'election/view_candidate.html', {'var':'v'})

def update_candidate(request, id):
    if request.method == 'GET':
        candidate_instance = Candidates.objects.get(pk=id)
        form = CandidatesForm(instance=candidate_instance)
        return render(request, 'election/update_candidate.html',{'var':'v', 'form': form})

    else:
        candidate_instance = Candidates.objects.get(pk=id)
        form = CandidatesForm(request.POST, instance= candidate_instance)
        if form.is_valid():
            form.save()
        return redirect('view_candidate')



def delete_candidate(request, id):
    candidate_instance = Candidates.objects.get(pk=id)
    candidate_instance.delete()
    return redirect('view_candidate')




# view (controler) methods for candidates ends here




# view (controler) methods for regions starts here


def register_region(request):
    if request.method == 'GET':
        form = RegionsFrom()
        return render(request, 'election/create_region.html', {'form': form, 'var':'r'})

    else:
        form = RegionsFrom(request.POST)
        if form.is_valid():
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'election/create_region.html', {'form': form, 'var':'r'})
        return redirect('register_region')




def view_region(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        region_data = Regions.objects.all()
        return render(request, 'election/view_region.html', {'var':'v', 'region_data':region_data})
    
    elif request.method == 'POST' and not (request.POST.get('search') ==''):
        region_data = Regions.objects.all().filter(region_name__icontains=request.POST.get('search'))
        return render(request, 'election/view_region.html', {'var':'v', 'region_data':region_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'election/view_region.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'election/view_region.html', {'var':'v'})

def update_region(request, id):
    if request.method == 'GET':
        region_instance = Regions.objects.get(pk=id)
        form = RegionsFrom(instance=region_instance)
        return render(request, 'election/update_region.html',{'var':'v', 'form': form})

    else:
        region_instance = Regions.objects.get(pk=id)
        form = RegionsFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('view_region')



def delete_region(request, id):
    region_instance = Regions.objects.get(pk=id)
    region_instance.delete()
    return redirect('view_region')



# view (controler) methods for regions ends here





# view (controler) methods for polling stations starts here



def register_polling_station(request):
    if request.method == 'GET':
        form = PollingStationsForm()
        return render(request, 'election/create_polling_station.html', {'form': form, 'var':'r'})

    else:
        form = PollingStationsForm(request.POST)
        if form.is_valid():
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'election/create_polling_station.html', {'form': form, 'var':'r'})
        return redirect('register_polling_station')




def view_polling_station(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        polling_station_data = PollingStation.objects.all()
        return render(request, 'election/view_polling_station.html', {'var':'v', 'polling_station_data':polling_station_data})
    
    elif request.method == 'POST' and not (request.POST.get('search') ==''):
        polling_station_data = PollingStation.objects.all().filter(polling_station_name__icontains=request.POST.get('search'))
        return render(request, 'election/view_polling_station.html', {'var':'v', 'polling_station_data':polling_station_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'election/view_polling_station.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'election/view_polling_station.html', {'var':'v'})

def update_polling_station(request, id):
    if request.method == 'GET':
        polling_station_instance = PollingStation.objects.get(pk=id)
        form = PollingStationsForm(instance=polling_station_instance)
        return render(request, 'election/update_polling_station.html',{'var':'v', 'form': form})

    else:
        polling_station_instance = PollingStation.objects.get(pk=id)
        form = PollingStationsForm(request.POST, instance= polling_station_instance)
        if form.is_valid():
            form.save()
        return redirect('view_polling_station')



def delete_polling_station(request, id):
    polling_station_instance = PollingStation.objects.get(pk=id)
    polling_station_instance.delete()
    return redirect('view_polling_station')



# view (controler) methods for polling stations ends here





# view (controler) methods for observers starts here



def register_observer(request):
    if request.method == 'GET':
        form = ObserverForm()
        return render(request, 'election/create_observer.html', {'form': form, 'var':'r'})

    else:
        form = ObserverForm(request.POST)
        if form.is_valid():
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'election/create_observer.html', {'form': form, 'var':'r'})
        return redirect('register_observer')




def view_observer(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        observer_data = Observer.objects.all()
        return render(request, 'election/view_observer.html', {'var':'v', 'observer_data':observer_data})
    
    elif request.method == 'POST' and not (request.POST.get('search') ==''):
        observer_data = Observer.objects.all().filter(observer_name__iexact=request.POST.get('search'))
        return render(request, 'election/view_observer.html', {'var':'v', 'observer_data':observer_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'election/view_observer.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'election/view_observer.html', {'var':'v'})

def update_observer(request, id):
    if request.method == 'GET':
        observer_instance = Observer.objects.get(pk=id)
        form = ObserverForm(instance=observer_instance)
        return render(request, 'election/update_observer.html',{'var':'v', 'form': form})

    else:
        observer_instance = Observer.objects.get(pk=id)
        form = ObserverForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('view_observer')



def delete_observer(request, id):
    observer_instance = Observer.objects.get(pk=id)
    observer_instance.delete()
    return redirect('view_observer')




# view (controler) methods for observers ends here




