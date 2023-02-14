from django.shortcuts import render
import random
import qrcode
# Create your views here.
otp = 0
def openLoginPage(request):
    return render (request,"login.html")

def validateuser(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")

    if username == "varun" and password == "shan":
        rno = random.randint(1000,9999)
        global otp
        otp = rno
        im = qrcode.make("OTP:"+str(rno))
        im.save(r"app/static/qrimages/varun.jpg")
        return render(request,"qrcode_page.html")
    else:
        return render(request,"login.html",{"message":"Invalid User"})

def validateOTP(request):
    user_otp = request.POST.get("otp")
    if user_otp == str(otp):
        return render(request,"welcome.html")
    else:
        return render(request,"login.html", {"message": "Invalid OTP"})
    