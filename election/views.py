import random
from typing import Type

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.fields.json import JSONField
from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import redirect, render
from systemuser.models import EvotingUser

from election.forms import VoterForm

from .forms import (CandidatesForm, ElectionForm, ElectionRegionsFrom,
                    ObserverForm, PartyForm, PollingStationsForm,
                    ReferendumForm, ReferendumOptionsForm, RegionsForm)
from .models import (ActionsToBeApproved, Candidates, Election, ElectionRegions, Observer, Party,
                     PollingStation, Referendum, ReferendumOptions, Regions,
                     Voter)
from .serializer import  RegionsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
import requests
from requests import Request, Session

def update_region_new(request, id, action, json_data):
    print(id)
    # region_instance = Regions.objects.get(id=id)
    # serializer = RegionsSerializer(region)
    # json_data = json.dumps(serializer.data)
    url = "http://127.0.0.1:8000/evoting_api2/region-update/"+ str(id) +"/"
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    r = requests.post(url, data=json_data, headers=headers)
    
    # serializer = RegionsSerializer(instance = region_instance, data= data)
    # if serializer.is_valid():
    #     serializer.save()
    return redirect('view_region')

def reject_approve_actions(request, id):
    approve_actions_instance = ActionsToBeApproved.objects.get(pk=id)
    approve_actions_instance.delete()
    return redirect('view_approve_actions')

def create_approve_actions(request, json_data, app_action_id):
    url = "http://127.0.0.1:8000/evoting_api2/region-create/"
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    r = requests.post(url, data= json_data, headers=headers)
    print("deleted by the api")
    action_insta =ActionsToBeApproved.objects.get(pk=app_action_id)
    action_insta.delete()
    print("action list wust yalewem tedeletual")
    return HttpResponse("ere addisem create argual")
def delete_approve_actions(request, id, app_action_id):
    url = "http://127.0.0.1:8000/evoting_api2/region-delete/"+ str(id) +"/"
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    r = requests.post(url, headers=headers)
    print("deleted by the api")
    action_insta =ActionsToBeApproved.objects.get(pk=app_action_id)
    action_insta.delete()
    print("action list wust yalewem tedeletual")

    return HttpResponse("entity has been succssfully deleted!")


def approve_actions(request, id):

    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('approve')=='Approve':
           
            approved_data = request.POST.get('entity_data')
            approved_data_as_dict = json.loads(approved_data)
            entity_id =request.POST.get('entity_id')
            approve_action_id  =request.POST.get('approve_actions_id')
            
            serializer = RegionsSerializer(data = approved_data_as_dict)
            if serializer.is_valid():
                json_data = json.dumps(serializer.data)
            if(request.POST.get('action_type')=='Update'):
                update_region_new(request, request.POST.get('entity_id'), 'Update', json_data)
            if(request.POST.get('action_type')=='Delete'):
                delete_approve_actions(request, entity_id , approve_action_id)
            if(request.POST.get('action_type')=='Create'):
                create_approve_actions(request, json_data, approve_action_id )
    #         if serializer.is_valid():
                
    #             serializer.save()
    #             approve_actions_instance = ActionsToBeApproved.objects.get(pk=id)
    #             approve_actions_instance.delete()
    #         else:
    #             print("didn't pass is_valid ")
    #             print(serializer.errors)
    return redirect('view_approve_actions')


def view_approve_actions(request):

    actions_data = ActionsToBeApproved.objects.all()
    post_data = request.POST

    if request.method == 'POST':
        if 'search_btn' in post_data:
            actions_data = ActionsToBeApproved.objects.filter(Q(sender__icontains=post_data.get('search')) | Q( entity__icontains =post_data.get('search')))
            return render(request, 'election/approve_actions.html', {'actions_data':actions_data})

        elif 'view_all' in post_data:
            return render(request, 'election/approve_actions.html', {'actions_data':actions_data})

    else:   
        
        return render(request, 'election/approve_actions.html',{'actions_data':actions_data} )


# view (controler) methods for view analytics starts here
def election_api(request):
    prosperity = 0
    semayawi = 0
    baytona = 0;
    netsanet_ena_ekulnet = 0;
    abc = 0;
    voters_vote =  Voter.objects.values_list('voted_to')
    print(voters_vote)
    for a in voters_vote:
        print ("here"+str(a[0]))
        h= Candidates.objects.all().filter(id=a[0])
    
        for a in h:
            a.number_of_votes = 0
            a.save()


# view (controler) methods for view analytics starts here



# view (controler) methods for view analytics starts here

def view_analytics(request):
    
    return render(request, 'election/view_analytics.html')


# view (controler) methods for cast a ballot starts here

def cast_ballot(request):
    candidates_data = Candidates.objects.all()
    parties_data  =Party.objects.all()
    context = {'candidates_data':candidates_data, 'parties_data':parties_data}
   
    return render(request, 'election/cast_ballot.html', context)

# view (controler) methods for referendum result starts here

def view_referendum_result(request):
    referendum_data = Referendum.objects.all()

    return render(request, 'election/view_referendum_result.html',{ 'referendum_data':referendum_data})

# view (controler) methods for referendum result starts here



# view (controler) methods for election result starts here

def view_election_result(request):
    parties_data = Party.objects.all()
    voters_data = Voter.objects.all()
    election_region_data = ElectionRegions.objects.all()
    candidates_data = Candidates.objects.all()
    votes = Voter.objects.values_list('voted_to')
    prr = Party.objects.get(party_name='Prosperity')
    pr=0; sm=0; ne=0; ab=0; by=0;
    print(votes)
    for a in votes:
        print(a[0])
        h= Candidates.objects.all().filter(id=a[0])
        
        for a in h:
            if not(a== None):
                c = str(a.party)
                if c == 'Prosperity':
                    pr+=1
                elif c == 'Semaywi':
                    sm+=1
                elif c=='Netsanet Ena Ekulnet':
                    ne+=1
                elif c=='abc':
                    ab+=1
                elif c=='Baytona':
                    by+=1
            print(pr)
    add = [pr,sm, ne, ab, by]
    print(add)
                       

    # for region in regions_data:
    #     abc =Regions.objects.get(region_name=region_name)
    #     polling_station_in_this_region= abc.pollingstation_set.all()
    
    context = {'parties_data': parties_data, 'election_region_data': election_region_data, 'candidates_data':candidates_data, 'h':h, 
    
                'add':add}

    return render(request, 'election/view_election_result.html', context)



# view (controler) methods for verify vote universally starts here
def verify_vote_universally(request):
    
    # i declared this to hide the "No result found text while the page is loading in 'GET'.
    method_is_get=True 

    if request.method == 'GET':
        regions = ElectionRegions.objects.all()
        polling_station=PollingStation.objects.all()
        context ={'var':'v', 'regions':regions, 'polling_station':polling_station, 'method_is_get': method_is_get}

        return render(request, 'election/verify_vote_universally.html',context)

    if request.method =='POST':
        if (request.POST.get('randorloc_choice') == 'Random'):
            regions = ElectionRegions.objects.all()
            polling_station=PollingStation.objects.all()
        
            # if request.POST.get('randorloc_choice') == 'bylocation':
            #     'location_type': ['Verify by Polling Station'],
            # 'regions': ['Oromia'], 'polling_stations': ['abc']}>
            total_voted_voter = len(Voter.objects.all().filter(~Q(voted_to=None)))
            thirty_percent_of_voter = ((total_voted_voter*30)/100)
            #Generate 30% of the total voters.. random numbers between 1 and total voters number
            randomlist = random.sample(range(1, total_voted_voter), int(thirty_percent_of_voter))
            # verification_data= Voter.objects.all().filter(pk=1)
            verification_data= Voter.objects.all().filter(pk__in=randomlist)
            context ={'var':'v', 'verification_data':verification_data, 'regions':regions, 'polling_station':polling_station, 'method_is_get': method_is_get}
            return render(request, 'election/verify_vote_universally.html',context)

        elif request.POST.get('randorloc_choice') == 'bylocation' and request.POST.get('location_type') == 'Verify by Region':
            regions = ElectionRegions.objects.all()
            polling_station=PollingStation.objects.all()
            region_name = request.POST.get('regions')
            print(region_name)
            abc =ElectionRegions.objects.get(region_name=region_name)
            polling_station_in_this_region= abc.pollingstation_set.all()
            byregion_verification_data =Voter.objects.all().filter(pk__in=polling_station_in_this_region)
            print(byregion_verification_data)
            context ={'var':'v', 'byregion_verification_data':byregion_verification_data, 'regions':regions, 'polling_station':polling_station, 'region_name':region_name}
            return render(request, 'election/verify_vote_universally.html',context)

        elif request.POST.get('randorloc_choice') == 'bylocation' and request.POST.get('location_type') == 'Verify by Polling Station':
            regions = ElectionRegions.objects.all()
            polling_station=PollingStation.objects.all()
            polling_station_name2= request.POST.get('polling_stations');
            print(polling_station_name2)
            abc =PollingStation.objects.get(polling_station_name=polling_station_name2)
            verification_data= abc.voted_place.all()
            print(verification_data)
            print(abc)
            context ={'var':'v', 'verification_data':verification_data, 'regions':regions, 'polling_station':polling_station, # i declared this to hide the "No result found text while the page is loading in 'GET'
}
            return render(request, 'election/verify_vote_universally.html',context)

        
        else:
            print('random is not selected')
            return render(request, 'election/verify_vote_universally.html')

# view (controler) methods for verify vote individually starts here

def verify_vote_individually(request):
    
    if request.method == 'POST':
        verification_data= Voter.objects.all().filter(voter_registratio_id = request.POST.get('search'))
        return render(request, 'election/verify_vote_individually.html', {'var':'v', 'verification_data':verification_data})

    else:
        method_is_get=True;
        return render(request, 'election/verify_vote_individually.html', {'var':'v', 'method_is_get': method_is_get})
    return

def view_live_vote_counter(request):
    
    return render(request,'election/view_live_votes_counter.html')


def fetch_vote_data(request):
    
    vote_data = len(Voter.objects.filter(~Q(voted_to=None)))
   
    return JsonResponse({'vote_data':vote_data})


def view_live_voters_counter(request):
    # data = len(EvotingUser.objects.all())

    return render(request,'election/view_live_voters_counter.html')

def fetch_voter_data(request):
    data = Voter.objects.count()
    # data2 = EvotingUser.objects.all()

    # return JsonResponse({"data":list(data2.values())})
    return JsonResponse({'data':data})



# view (controler) methods for Voter starts here

@login_required(login_url='login')
def register_voter(request):
    if request.method == 'GET':
        form = VoterForm()
        return render(request, 'election/create_voter.html', {'form': form, 'var':'r'})

    else:
        form = VoterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(request.POST)
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'election/create_voter.html', {'form': form, 'var':'r'})
        return redirect('register_voter')




def view_voter(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        print(request.POST)
        voter_data = Voter.objects.all()
        # voters_vote =  Voter.objects.values_list('voted_to')
        # print(voters_vote)
        # for a in voters_vote:
        #     print ("here"+str(a[0]))
        #     h= Candidates.objects.all().filter(id=a[0])
        
        #     for a in h:
        #         a.number_of_votes = 0
        #         a.save()
        #         print("there" + str(a.number_of_votes))
        #         a.number_of_votes = a.number_of_votes + 1
        #         a.save()
        return render(request, 'election/view_voter.html', {'var':'v', 'voter_data':voter_data, 'request':request})
    
    elif request.method == 'POST':
        voter_data = Voter.objects.all().filter(first_name=request.POST.get('search'))
        return render(request, 'election/view_voter.html', {'var':'v', 'voter_data':voter_data, 'user':request.user})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'election/view_voter.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'election/view_voter.html', {'var':'v'})

@login_required()
def update_voter(request, id):
    if request.method == 'GET':
        voter_instance = Voter.objects.get(pk=id)
        form = VoterForm(instance=voter_instance)
        return render(request, 'election/update_voter.html',{'var':'v', 'form': form})

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
        referendum_data = Referendum.objects.all()
        return render(request, 'election/view_referendum.html', {'var':'v', 'referendum_data':referendum_data})
    
    elif request.method == 'POST' and not (request.POST.get('search') ==''):
        referendum_data = Referendum.objects.all().filter(referendum_name__icontains=request.POST.get('search'))
        return render(request, 'election/view_referendum.html', {'var':'v', 'referendum_data':referendum_data})

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
        regions = ElectionRegions.objects.all()
        context= {'var':'v', 'candidate_data':candidate_data, 'regions':regions }
        return render(request, 'election/view_candidate.html', context)
    
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
        form = RegionsForm()
        return render(request, 'election/create_region.html', {'form': form, 'var':'r'})

    else:
        form = RegionsForm(request.POST)
        if form.is_valid():
            region = form.save(commit=False)
            serializer = RegionsSerializer(region)
            json_data = json.dumps(serializer.data)


            # url = "http://127.0.0.1:8000/evoting_api2/region-create/"
            # headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

            # s = Session()
            # req = Request('POST', url=url, headers=headers)
            # prepped = req.prepare()

            # # do something with prepped.body
            # prepped.body = json_data
            # # del prepped.headers[ 'Content-type': 'application/json']

            # resp = s.send(prepped,
                
            #     timeout=10
            # )
            data = serializer.data
            # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            # r = requests.post(url, data=json_data, headers=headers)
            # r1 = requests.post('http://127.0.0.1:8000/evoting_api2/region-create/')  
            actions = ActionsToBeApproved();
            actions.sender = request.user
            print(vars(region))
            actions.entity_id = 1
            actions.action_type  ='Create'
            actions.data_type = type(region)
            actions.entity = json_data
            actions.save()
            print(vars(actions))
            # form.save_m2m()
        else:
             return render(request, 'election/create_region.html', {'form': form, 'var':'r'})
        return redirect('register_region')




def view_region(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        region_data =Regions.objects.all()
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
        form = RegionsForm(instance=region_instance)
        return render(request, 'election/update_region.html',{'var':'v', 'form': form})

    else:
        region_instance = Regions.objects.get(pk=id)
        form = RegionsForm(request.POST)
        if form.is_valid():
            
            
            region = form.save(commit=False)
            region.id =id;
            print(region.seats_for_HPR)
            print(vars(region))
            print(region.id)
            print(type(region))
            serializer = RegionsSerializer(region)
            json_data = json.dumps(serializer.data)
            ab= str.split(str(type(region)),'.')
            abc = ab[2]
            actions = ActionsToBeApproved();
            actions.sender = request.user
            actions.entity_id = id
            actions.action_type  ='Update'
            actions.data_type = 'Regions'
            actions.entity = json_data
            actions.save()
            print(vars(actions))
            # url = "http://127.0.0.1:8000/evoting_api2/region-update/"+ str(id) +"/"
            # headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            # r = requests.post(url, data=json_data, headers=headers)
        return redirect('view_region')



def delete_region(request, id):
    region = Regions.objects.get(pk=id)
    serializer = RegionsSerializer(region)
    json_data = json.dumps(serializer.data)
    actions = ActionsToBeApproved();
    actions.sender = request.user
    actions.entity_id = id
    actions.action_type  ='Delete'
    actions.entity = json_data
    actions.save()
    return redirect('view_region')


# view (controler) methods for election regions ends here



# view (controler) methods for election regions starts here


def register_election_region(request):
    if request.method == 'GET':
        form = ElectionRegionsFrom()
        return render(request, 'election/create_election_region.html', {'form': form, 'var':'r'})

    else:
        form = ElectionRegionsFrom(request.POST)
        if form.is_valid():
            form.save()
            # form.save_m2m()
        else:
             return render(request, 'election/create_election_region.html', {'form': form, 'var':'r'})
        return redirect('register_election_region')




def view_election_region(request):
    
    if request.method == 'POST' and request.POST.get('search') == '__all__':
        election_region_data = ElectionRegions.objects.all()
        return render(request, 'election/view_election_region.html', {'var':'v', 'election_region_data':election_region_data})
    
    elif request.method == 'POST' and not (request.POST.get('search') ==''):
        election_region_data = ElectionRegions.objects.all().filter(election_region_name__icontains=request.POST.get('search'))
        return render(request, 'election/view_region.html', {'var':'v', 'election_region_data':election_region_data})

    elif request.method == 'GET':
        method_is_get=True;
        return render(request, 'election/view_election_region.html', {'var':'v', 'method_is_get': method_is_get})
    else:
        return render(request, 'election/view_election_region.html', {'var':'v'})

def update_election_region(request, id):
    if request.method == 'GET':
        election_region_instance = ElectionRegions.objects.get(pk=id)
        form = ElectionRegionsFrom(instance=election_region_instance)
        return render(request, 'election/update_election_region.html',{'var':'v', 'form': form})

    else:
        election_region_instance = ElectionRegions.objects.get(pk=id)
        form = ElectionRegionsFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('view_election_region')



def delete_election_region(request, id):
    election_region_instance = ElectionRegions.objects.get(pk=id)
    election_region_instance.delete()
    return redirect('view_election_region')



# view (controler) methods for electionregions ends here





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




