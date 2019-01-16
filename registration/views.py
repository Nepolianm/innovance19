from django.shortcuts import render
from .models import Registration


# Create your views here.
def registration(request):
    return render(request, "exetera.htm", {})


def register(request):
    if request.method != 'POST':
        return render(request, "registration.html", {})

    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    college = request.POST.get('college')
    is_ieee = True if request.POST.get('ieee_member') == '1' else False
    member_id = request.POST.get('member_id')
    tshirt = request.POST.get('tshirt')
    is_veg = True if request.POST.get('is_veg') == 1 else False
    accom = True if request.POST.get('accom_needed') == 1 else False

    r = Registration.objects.create(name=name, email=email, mob=phone, college=college,
                                    is_ieee_member=is_ieee, member_id=member_id,
                                    t_shirt_size=tshirt, accommodation=accom, is_veg=is_veg)
    if r:
        # success
        return render(request, "success.html", {})
    else:
        return render(request, "failed.html", {})
    # fetch the data
    # create row in table
    # return acknowldegement page
