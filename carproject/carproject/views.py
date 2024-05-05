from django.shortcuts import render
from carfirst.models import Notification
from django.http import HttpResponse
from twilio.rest import Client

account_sid = 'AC64e061de81bc61a9c7c2a687f4eb8837'
auth_token = '318bdad7c42c9b663cb41981169bad69'

twillio_number = '+12013992626'
target_number = '+917284047777'

client = Client(account_sid,auth_token)

# Create your views here.
def submitafter(request):
    username = request.GET["username"]
    place_name = request.GET["place_name"]
    data = request.GET["date"]
    phone_no = request.GET["phone_no"]
    number_of_passenger = request.GET["number_of_passenger"]
    vehicle_required = request.GET["vehicle_required"]

    res=Notification(username=username,place_name=place_name,date=data,phone_no=phone_no,number_of_passenger=number_of_passenger,vehicle_required=vehicle_required)
    res.save()
    # mydata = Notification.objects.all().values()

    context = [ 'username :'+ username + ' Destination : ' + place_name+ ' Date:' + data+' Phone no. :' + phone_no+' Passengers :' + number_of_passenger+' Vehicle required :' + vehicle_required ]
    message = client.messages.create(
    body=context,
    from_=twillio_number,
    to=target_number 
    )
    print(message.body)

    return render(request,'home.html')

def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")

def notify(request):
    return render(request,"notify.html")

# def sendmessage(request):
#     myData = Notification.objects.all().values()
#     context = {
#         'data' : myData
#     }
#     return render(request,"home.html")




