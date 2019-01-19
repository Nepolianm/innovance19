import datetime
import urllib

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from innovance import settings
from django.shortcuts import render
from .models import Registration
from datetime import datetime
import json


# Create your views here.
@csrf_exempt
def registration(request):
    return render(request, "exetera.htm", {})


# def register(request):
#     if request.method != 'POST':
#         return render(request, "registration.html", {})
#
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     phone = request.POST.get('phone')
#     college = request.POST.get('college')
#     is_ieee = True if request.POST.get('ieee_member') == '1' else False
#     member_id = request.POST.get('member_id')
#     tshirt = request.POST.get('tshirt')
#     is_veg = True if request.POST.get('is_veg') == 1 else False
#     accom = True if request.POST.get('accom_needed') == 1 else False
#     referral = request.POST.get('referral_code')
#
#     r = Registration.objects.create(name=name, email=email, mob=phone, college=college,
#                                     is_ieee_member=is_ieee, member_id=member_id,
#                                     t_shirt_size=tshirt, accommodation=accom, is_veg=is_veg,
#                                     referral_code=referral)
#     if r:
#         # success
#         # send sms
#         message = "Hi %s,\nYou have successfully registered for Innovance '19, on %s.\nYour ID is %s.\nReach us at " \
#                   "http://innovance19.in\nThank you :)"
#         today = datetime.now().strftime("%d %B %Y")
#         x = send_sms(r.mob, message % (name, today, str(r.id)))
#         print(x)
#         return render(request, "success.html", {})
#     else:
#         return render(request, "failed.html", {})
#     # fetch the data
#     # create row in table
#     # return acknowldegement page


def send_sms(recepient, message):
    data = urllib.parse.urlencode({'apikey': settings.TEXTLOCAL_APIKEY, 'numbers': recepient,
                                   'message': message})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return (fr)


@csrf_exempt
def complete_payment(request):
    if request.method != "POST":
        return HttpResponse("<h1>Not Found</h1>")

    data = request.POST.get("data")
    json_data = json.loads(data)
    email = json_data['userEmailId']
    print("json %s" % data)
    print("email %s " % email)

    name = json_data['userName']
    ticketPrice = json_data['ticketPrice']
    answerList = json.loads(json_data['answerList'])
    order_id = json_data['uniqueOrderId']
    timestamp = json_data['registrationTimestamp']
    print("name %s\nprice %s\nanswerList " % (name, ticketPrice), answerList)
    print("order_id %s\n timestamp %s" % (order_id, timestamp))
    # user = Registration.objects.get(email=email)
    # user.is_paid = True
    # user.save()
