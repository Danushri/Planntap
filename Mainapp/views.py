from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404, QueryDict
from Mainapp.forms import Registration_form, Index_form
from django.views.generic import TemplateView
from Mainapp.models import Diary
from django.core.mail import send_mail
import json
from django.core.serializers import serialize
from django.contrib.auth.models import User


class AddDiaryView (TemplateView): #inherits from TemplateView built into django
    template_name = 'Mainapp2/addDiary.html'

    def get(self, request): # GET requestes rooted to this method  - used for dispatch method to interpret type of request
        form = Index_form()

        args = {

        'form' :form,

        }
        return render(request, self.template_name, args )

    def post (self, request):
        formRes = Index_form(request.POST, request.FILES)
        print(formRes)
        if formRes.is_valid ():
            # print(request.POST['image'])
            post = formRes.save(commit = False)
            post.member = request.user

            post.save() #save image in folder
            post.Image = 'static/Mainapp/images/' + str(formRes.cleaned_data['Image'])
            post.save() #save the correct location of image
            form = Index_form()

            args = {
            'Eventname' : formRes.cleaned_data['Eventname'],
            'desc' : formRes.cleaned_data['desc'],

            }
            return render(request, 'Mainapp2/EntrySuccess.html', args)

            args = {

                'form':form,
                'text' : text

            }


        return render(request, self.template_name, args)




def EntrySuccess (request):

    return render(request, 'Mainapp2/EntrySuccess.html')



def index(request):

    return render(request, 'Mainapp2/index.html')



def get_diaryEntry(request):
    user = User.objects.get(username=request.user)
    posts = Diary.objects.filter(member=user)
    print(posts)
    postList = json.loads(serialize('json', posts))
    print(postList)

    return JsonResponse({
        'diaryEntry' : postList

    })

def login(request):
	loginForm = Login_form()
	return render(request,'Mainapp2/login.html' ,{'form':loginForm})

def register (request):
    if request.method == 'POST':

        form = Registration_form(request.POST)
        if form.is_valid():
            form.save()
            subject = "Planntap Register"
            message = "Thanks for registering"
            from_email = "DanushriWeb@gmail.com"
            recipient_list= [form.cleaned_data["email"]]
            send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list, fail_silently=False)
            return redirect('index')
        else:
            print('Form Failed')
            return redirect('register')
    else:
        form = Registration_form ()
        context = {

        'reg_form' : form

        }

    return render(request, 'Mainapp2/register.html', context )

import googlemaps
import pprint
import time
import json
from django.core.serializers import serialize
import random


def maps (request):
    API_KEY = 'AIzaSyASprX-jzfE67JZ3KLVKfxUCQfIjyjQoIw'

    gmaps = googlemaps.Client(key=API_KEY)

    places_result = gmaps.places_nearby(location='-33.8670522,151.1957362', radius=4000, open_now=True, type = 'food')
    # all_places = places_result.get('results')
    # arr = []
    # for i in all_places:
    #     arr.append(i.get("name"))
    # length = len(arr)
    # randomNum = random.randint(0,length-1)
    # print('RANDOM: ', randomNum)
    # print(arr[randomNum])

    pprint.pprint(places_result)

    # details = gmaps.get_place_details()
    # print(details)

    args = {
    'places_result' : places_result

    }



    return render(request, 'Mainapp2/maps.html', )

import urllib3
import facebook
import requests
from datetime import datetime


def facebookEvent(request):

    token = 'EAAC7SjbyGTUBAAZCEu9ZAApDnxZCvU9U2y8a6snFgYvZACrmkSYhTaQ3vZAevZCjFeHp0kn14QDY5xVdfY24yRlZB4A5vqWZCJrm5JtPjqsGK5IslXuIC6uypyUOp5v8RNyoise5v2oG2sC4GU0ox6uZAwbbyqZCaLzAlZASggCF9ILSgZDZD'
    graph = facebook.GraphAPI(token)
    # fields = ["description , name"]
    event_ids = ['1693565647448194', '218706842669473']
    eventsArray = []





    events = graph.get_objects(ids=event_ids,fields = 'description , name, start_time')
    # print(json.dumps(events, indent = 4))
    print(json.dumps(events))





    print(events['1693565647448194'])
    test = "Danushri"
    ctr = 0
    for event in events :
        eventsArray.append(events[event_ids[ctr]])
        print(ctr)
        print(events[event_ids[ctr]])
        ctr = ctr + 1


    context = {

        'events':eventsArray,
        # 'event':test
        'ids':event_ids
    }


    return render(request, 'Mainapp2/facebook.html', context)

def Random(request):

    return render(request, 'Mainapp2/Random.html')

def RandomButton(request):
    API_KEY = 'AIzaSyASprX-jzfE67JZ3KLVKfxUCQfIjyjQoIw'

    gmaps = googlemaps.Client(key=API_KEY)

    places_result = gmaps.places_nearby(location='51.5228196814,-0.0430759562', radius=2000, open_now=True, type = 'cafe')
    all_places = places_result.get('results')
    arr = []
    for i in all_places:
        arr.append(i)
    length = len(arr)
    randomNum = random.randint(0,length-1)
    place = arr[randomNum]
    print(place)




    return JsonResponse({
        'place' : place,
    })

def deleteDiary (request):
    try:
        # delete = QueryDict(request.body)
        print("entered try")
        list1 = list(request)
        stringed = str(list1)
        splitVal = stringed.split("'")
        id = int(splitVal[1])
        #deleteDiaryentry = Diary.objects.get(pk = delete.get('id'))
        deleteDiaryentry = Diary.objects.get(pk = id)
        deleteDiaryentry.delete()
        print("delete success")

        return JsonResponse({
            'response' : 'return delete response',
            'values' : id,

        })
    except:
        Http404(request)

def updateDiary(request):

    UpdateDict = QueryDict(request.body)
    Diary_id = UpdateDict.get('id')
    diaryUpdate = Diary.objects.get(pk=Diary_id)
    diaryUpdate.Eventname = UpdateDict.get('update_event_name')
    diaryUpdate.desc = UpdateDict.get('update_desc')
    diaryUpdate.Location = UpdateDict.get('update_Location')
    diaryUpdate.Date = UpdateDict.get('update_Date')
    diaryUpdate.Rating = UpdateDict.get('update_Rating')
    diaryUpdate.Review = UpdateDict.get('update_Review')
    diaryUpdate.save()
    return JsonResponse({
        'update' : 'Updated'
    })

import tweepy
import sys

def twitter(request):
    print('My name is Danushri')
    auth = tweepy.OAuthHandler('ypwCWnoUVmTrNiTjMujzpOvh7', '8IU2ZWDwf6aPra7sRrxBNpkVW71pItgGI6HAiIcBPZ8JrAarnQ')
    auth.set_access_token('1233854503616745472-N1CSQimnLcbRaOKM6Wwrl2PLo1CLd1', 'hrFPXQN2CGAxhC1a8IxVosgDehxgJhByH5biCMd7BWhbS')
    api = tweepy.API(auth)

    public_tweets=api.home_timeline()
    top20 = api.mentions_timeline()
    print(top20)

    args = {
        'top20' : top20,
    }
    #api.update_status('I just went to ' + eventname + " " + decription)

    return render(request, 'Mainapp2/twitter.html', args)
