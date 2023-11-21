from django.core.files.storage import FileSystemStorage
from django.db import connection
from django.http import HttpResponse, request, JsonResponse
from django.shortcuts import render, redirect
from . models import *
import datetime
# Create your views here.log

def forgot(request):
    global gmail
    if request.method=='POST':
        u = request.POST['textfield']
        f = connection.cursor()
        f.execute("select * from freelancer_login where username='" + u + "'")
        q = f.fetchone()
        if q is None:
            return HttpResponse("<script>alert('User does not exists');window.location='/freelancer/forgot/';</script>")
        else:
            import smtplib
            from email.mime.text import MIMEText

            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)

                gmail.ehlo()

                gmail.starttls()

                gmail.login('freelancemp7@gmail.com', 'freelancer@')

            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText("Your Password is " + q[2])

            msg['Subject'] = 'Verification'

            msg['To'] = u

            msg['From'] = 'freelancemp7@gmail.com'

            try:

                gmail.send_message(msg)
                return login1(request)

            except Exception as e:

                print("COULDN'T SEND EMAIL", str(e))

    return render(request,"forgot.html")

def login1(request):
    return render(request,"loginindex.html")
def adminhome(request):
    if request.session['lin'] == "l":
        return  render(request,"admin/adminhome.html")
    return login1(request)
def homepage(request):
    return render(request, "homepage.html")
def logpost(request):
    try:
        u=request.POST['textfield2']
        p=request.POST['textfield']
        obj=login.objects.get(username=u,password=p)
        lid=obj.id
        request.session['lid']=lid
        request.session['lin']="l"
        if obj.types=='admin':
            return redirect('/freelancer/adminhome/')
        elif obj.types=='freelancer':
            return redirect('/freelancer/freelancerhome/')
        elif obj.types == 'client':
            return redirect('/freelancer/clienthome/')
        else:
            return HttpResponse("nooooooo")
    except Exception as e:
        return HttpResponse("<script >alert('User not found');window.location='/freelancer/login1/'</script>")


def cregister(request):

        if request.method == "POST":
            name = request.POST['textfield']
            place = request.POST['textfield4']
            pin = request.POST['textfield5']
            email = request.POST['textfield2']
            phone = request.POST['textfield3']
            photo = request.FILES['fileField']
            password = request.POST['textfield7']
            confirmpassword = request.POST['textfield8']

            if password==confirmpassword:

               f = FileSystemStorage()
               cname = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
               f.save(r"C:\Users\hp\PycharmProjects\freelance_marketplace\freelancer\static\\" + cname + ".jpg", photo)
               path = "/static/" + cname + ".jpg"
               op = login()
               op.username = email
               op.password = password
               op.types = 'client'
               op.save()
               # a=bank()
               # a.bankname="SBI"
               # a.account="123456789"
               # a.ifsc_code="123123"
               # a.mainbalance="1000000"
               # # a.clogin=op
               #a.save()
               obj = client()
               obj.cname = name
               obj.cplace = place
               obj.cpin = pin
               obj.cemail = email
               obj.cphone = phone
               obj.cphoto = str(path)
               obj.clogin = op
               obj.save()
               return HttpResponse("<script>alert('success !');window.location='/freelancer/login/'</script>")

        else:
            return render(request, "client/clientreg_index.html")

def fregister(request):

        if request.method == "POST":
            name = request.POST['textfield']
            place = request.POST['textfield4']
            post = request.POST['textfield6']
            pin = request.POST['textfield5']
            email = request.POST['textfield2']
            phone = request.POST['textfield3']
            experiance=request.POST['textarea2']
            photo = request.FILES['fileField']
            skill = request.POST['textarea']
            password = request.POST['textfield7']
            confirmpassword = request.POST['textfield8']

            f = FileSystemStorage()
            fname = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            f.save(r"C:\Users\hp\PycharmProjects\freelance_marketplace\freelancer\static\\" + fname + ".jpg", photo)
            path = "/static/" + fname + ".jpg"
            op = login()
            op.username = email
            op.password = password
            op.types = 'freelancer'
            op.save()
            obj = freelancers()
            obj.fname = name
            obj.fplace = place
            obj.fpost = post
            obj.fpin = pin
            obj.femail = email
            obj.fcontact = phone
            obj.fexperiance = experiance
            obj.fphoto = str(path)
            obj.skill = skill
            obj.flogin = op
            obj.save()
            return HttpResponse("<script>alert('success !');window.location='/freelancer/login/'</script>")
        else:
            return render(request, "freelance/freelancerreg_index.html")

def viewclients(request):
    if request.session['lin'] == "l":
        ob=client.objects.filter()
        return render(request,"admin/viewclient.html",{'p':ob})
    return login1(request)

def viewclients_more(request,id):
    if request.session['lin'] == "l":
        ob=client.objects.get(id=id)
        return render(request,"admin/viewmoreclientprofile.html",{'p':ob})
    return login1(request)
def crs(request,id):
    if request.session['lin'] == "l":
        c = requiredservice.objects.filter(clogin_id=id)
        return render(request, "admin/clientreqs.html", {'p': c})
    return login1(request)

def viewfreelancers(request):
    if request.session['lin'] == "l":
        ob = freelancers.objects.filter()
        return render(request,"admin/viewfreelancer.html",{'p':ob})
    return login1(request)

def viewfreelancers_more(request,id):

    if request.session['lin'] == "l":
        ob=freelancers.objects.get(id=id)
        return render(request,"admin/viewmorefreelancerprofile.html",{'p':ob})
    return login1(request)
def feedbacks(request,id):
    if request.session['lin'] == "l":
        ob = connection.cursor()
        ob.execute("select * from freelancer_feedback,freelancer_service_request,freelancer_service,freelancer_freelancers,freelancer_client where freelancer_feedback.serreqid_id=freelancer_service_request.id and freelancer_service_request.serviceid_id=freelancer_service.id and freelancer_service.flogin_id=freelancer_freelancers.id and freelancer_service_request.clogin_id=freelancer_client.id and freelancer_freelancers.id='" + str(id) + "'")
    # ob.execute("select * from freelancer_feedback,freelancer_freelancers,freelancer_client,freelancer_service_request,freelancer_service where  freelancer_service_request.serviceid_id=freelancer_service.id and freelancer_service_request.clogin_id=freelancer_client.id and freelancer_feedback.serreqid_id=freelancer_service_request.id and freelancer_service.flogin_id=freelancer_freelancers.id and freelancer_client.clogin_id='"+str(request.session['lid'])+"'")
        ob1 = ob.fetchall()
        return render(request,"admin/avfeedback.html", {'p': ob1})
    return login1(request)
def offeredservice(request,id):
    if request.session['lin'] == "l":
        # ob1=freelancers.objects.get(id=id)
        ob = service.objects.filter(flogin=id)
        return render(request, "admin/viewserviceoffered.html", {'p': ob})
    return login1(request)

def fcomplaints(request):
    if request.session['lin'] == "l":
        ob =connection.cursor()
        ob.execute("select * from freelancer_fcomplaint,freelancer_freelancers where freelancer_freelancers.id=freelancer_fcomplaint.fl_loginid_id")
        ob1=ob.fetchall()
        return render(request,"admin/fcomplaint.html",{'p':ob1})
    return login1(request)

def freplays(request,id):
    if request.session['lin'] == "l":
        ob = fcomplaint.objects.get(id=id)
        return render(request,"admin/fcomplaintreplay.html",{'p':id})
    return login1(request)
def fcomppost(request,id):
    if request.session['lin'] == "l":
            try:
                u = request.POST['textarea']
                obj = fcomplaint.objects.filter(id= id)
                obj.update(replay=u)
                return fcomplaints(request)

            except Exception as e:
                print(e)
    return login1(request)

def ccomplaints(request):
    if request.session['lin'] == "l":
        ob = connection.cursor()
        ob.execute("select * from freelancer_ccomplaint,freelancer_client where freelancer_client.id=freelancer_ccomplaint.clogin_id")
        ob1 = ob.fetchall()
        return render(request,"admin/ccomplaint.html",{'p':ob})
    return login1(request)

def creplays(request,id):
    if request.session['lin'] == "l":
        ob = ccomplaint.objects.get(id=id)
        return render(request,"admin/ccomplaintreplay.html",{'p':id})
    return login1(request)

def ccomppost(request,id):
    if request.session['lin'] == "l":
            try:
                u = request.POST['textarea']
                obj = ccomplaint.objects.filter(id= id)
                obj.update(replay=u)
                return ccomplaints(request)

            except Exception as e:
                print(e)
    return login1(request)

def sendnot(request):
    if request.session['lin'] == "l":
    # ob = notification.objects.filter()
        return render(request,"admin/sendnotification.html")
    return login1(request)

def nto(request):
    if request.session['lin'] == "l":
        if request.method=="POST":
            to=request.POST['a']
            if to=="client":
                cl=client.objects.all()
                return render(request, "admin/sendnotification.html",{'c':cl})
            else:
                fl=freelancers.objects.all()
                return render(request, "admin/sendnotification.html",{'f':fl})
        else:
            return render(request,"admin/sendnotification.html")
    return login1(request)

def sendnotif(request,id):
    if request.session['lin'] == "l":
        d=client.objects.get(id=id)
        return render(request, "admin/sendnot.html",{'clid':d.id})
    return login1(request)

def notifpost(request,id):
    if request.session['lin'] == "l":
        a = request.POST['textarea']
        d = client.objects.get(id=id)
        obj = notification()
        obj.to="client"
        obj.notification=a
        import datetime
        obj.ndate=datetime.datetime.now().strftime("%Y-%m-%d")
        obj.nclientid=d
        # obj.nfreelancerid="0"
        obj.save()
        # return HttpResponse("OOKK")
        return HttpResponse("<script >alert('success !');window.location='/freelancer/snotifications/'</script>")
        # return HttpResponse("<div class=progress-bar progress-bar-striped active></div>")


    return login1(request)

def sendnotif1(request,id):
    if request.session['lin'] == "l":
        d = freelancers.objects.get(id=id)
        return render(request, "admin/sendnot_f.html",{'flid':d.id})
    return login1(request)

def notifpost1(request,id):
    if request.session['lin'] == "l":
        a = request.POST['textarea']
        d = freelancers.objects.get(id=id)
        obj = notification_f()
        obj.to="freelancer"
        obj.notification=a
        import datetime
        obj.ndate=datetime.datetime.now().strftime("%Y-%m-%d")
        # obj.nclientid="0"
        obj.nfreelancerid=d
        obj.save()
        return HttpResponse("<script>alert('success !');window.location='/freelancer/snotifications/'</script>")
    return login1(request)
#freelancer

def freelancerhome(request):
    if request.session['lin'] == "l":
        # ob = connection.cursor()
        # ob.execute("select * from freelancer_freelancers where freelancer_freelancers.flogin_id='"+str(request.session['lid'])+"'")
        # ob.fetchall()
        return  render(request,"freelance/freelancer_index.html")
    # , {'p': ob}
    return login1(request)

#def updateprof(request):
    #obj=freelancers.objects.get(flogin=request.session['lid'])
    #return render(request,"freelance/updateprofile.html",{'d':obj})
def profileupdate(request):
    if request.session['lin'] == "l":
            if request.method=="POST":
                ob = freelancers.objects.get(flogin=request.session['lid'])

                a = request.POST['textfield']
                b = request.POST['textfield2']
                c = request.POST['textfield3']
                d = request.POST['textfield4']
                e = request.POST['textfield5']
                z = request.POST['textfield6']
                g = request.POST['textarea']
                h = request.POST['textarea2']
                i=request.FILES['fileField']

                f=FileSystemStorage()
                fname=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
                f.save(r"C:\Users\hp\PycharmProjects\freelance_marketplace\freelancer\static\\"+fname+".jpg",i)
                path="/static/"+fname+".jpg"
                obj=freelancers()
                obj.fname=a
                obj.fplace = b
                obj.fpost = c
                obj.fpin=d
                obj.femail=e
                obj.fcontact=z
                obj.fexperiance=g
                obj.skill=h
                obj.fphoto=str(path)
                obj.id=ob.id
                obj.flogin=ob.flogin
                obj.save()
                return HttpResponse("<script>alert('success !');window.location='/freelancer/profileupdate/'</script>")
            else :
               obj = freelancers.objects.get(flogin=request.session['lid'])
            return render(request, "freelance/updateprofile.html", {'d': obj})
    return login1(request)


def postservices(request):
    if request.session['lin'] == "l":

        return render(request,"freelance/postservice.html")
    return login1(request)

def servicepost(request):
    if request.session['lin'] == "l":
        try:
            u = request.POST['textfield']
            v = request.POST['textarea']
            z = request.POST['textfield3']
            obj = service()
            obj.service = u
            obj.service_details = v
            obj.price = z
            obj.flogin=freelancers.objects.get(flogin=request.session['lid'])
            obj.save()
            return postservices(request)
        except Exception as e:
            print(e)
    return login1(request)



def  viclients(request):
    if request.session['lin'] == "l":
        ob = client.objects.filter()                        #select_related("fclientid")
        return render(request,"freelance/viewclientprofile.html",{'p':ob})
    return login1(request)

def viclientsmore(request,id):
    if request.session['lin'] == "l":
        ob=client.objects.get(id=id)
        return render(request,"freelance/viewmoreclientprofile.html",{'p':ob})
    return login1(request)

def viewnot(request):
    if request.session['lin'] == "l":
        op=freelancers.objects.get(flogin=request.session['lid'])
        ob = notification_f.objects.filter(nfreelancerid=op.id)
        return render(request,"freelance/viewnotifications.html",{'p':ob})
    return login1(request)

def scomplaints(request):
    if request.session['lin'] == "l":
        ob = fcomplaint.objects.filter()
        return render(request,"freelance/sendcomplaint.html",{'p':ob})
    return login1(request)

def viewrep(request):
    if request.session['lin'] == "l":
        print(request.session['lid'])
        op = freelancers.objects.get(flogin=request.session['lid'])
        ob = fcomplaint.objects.filter(fl_loginid=op.id) #nfreelancerid
        return render(request,"freelance/viewreply.html",{'p':ob})
    return login1(request)

# def vfeedbacks(request):
#     # op = freelancers.objects.get(flogin=request.session['lid'])
#     # ob = feedback.objects.filter(ffreelancerid=op.id)
#     ob = connection.cursor()
#     ob.execute("select * from freelancer_feedback,freelancer_client,freelancer_freelancers,freelancer_service_request,freelancer_service where freelancer_service_request.id=freelancer_feedback.serreqid_id and freelancer_service.id=freelancer_service_request.serviceid_id and freelancer_freelancers.id=freelancer_service.flogin_id and freelancer_client.id=freelancer_service_request.clogin_id and freelancer_service.flogin_id='"+str(id)+"'")
#     o = ob.fetchall() #fclientid_id #ffreelancerid_id
#     return render(request,"freelance/urfeedback.html",{'p':o})


def vfeed(request):
    if request.session['lin'] == "l":
        # op = freelancers.objects.get(flogin=request.session['lid'])
        # ob = feedback.objects.filter(ffreelancerid=op.id)
        ob = connection.cursor()
        ob.execute("select * from freelancer_feedback,freelancer_client,freelancer_freelancers,freelancer_service_request,freelancer_service where freelancer_service_request.id=freelancer_feedback.serreqid_id and freelancer_service.id=freelancer_service_request.serviceid_id and freelancer_freelancers.id=freelancer_service.flogin_id and freelancer_client.id=freelancer_service_request.clogin_id and freelancer_freelancers.flogin_id='"+str(request.session['lid'])+"'")
        o = ob.fetchall() #fclientid_id #ffreelancerid_id
        return render(request,"freelance/urfeedback.html",{'p':o})
    return login1(request)

def vorders(request):
    if request.session['lin'] == "l":
        #op = freelancers.objects.get(flogin=request.session['lid'])
        #ob = postservice.objects.filter(nfreelancerid=op.id)
        ob = connection.cursor()
        ob.execute("select * from freelancer_service_request,freelancer_freelancers,freelancer_service,freelancer_client where freelancer_service_request.serviceid_id=freelancer_service.id and freelancer_service_request.clogin_id=freelancer_client.id and freelancer_freelancers.id=freelancer_service.flogin_id and freelancer_freelancers.flogin_id='"+str(request.session['lid'])+"'")
        o = ob.fetchall()
        return render(request,"freelance/verifyorder.html",{'p':o})
    return login1(request)

def oaccept(request,servicerid):
    if request.session['lin'] == "l":
        ob = service_request.objects.filter(id=servicerid)
        ob.update(status="accepted")
        return HttpResponse("accepted", {'p': id})
    return login1(request)


def oreject(request,servicerid):
    if request.session['lin'] == "l":
        ob = service_request.objects.filter(id=servicerid)
        ob.update(status="reject")
        return HttpResponse("rejected", {'p': id})
    return login1(request)

def scomp(request):
    if request.session['lin'] == "l":
        if request.method=="POST":
            comp=request.POST['textarea']
            import datetime
            date=datetime.datetime.now()
            print("jjjj")
            lid=request.session['lid']
            on=fcomplaint()
            on.complaint=comp
            on.cdate=date
            on.replay='pending'
            on.replaydate=date
            on.fl_loginid=freelancers.objects.get(flogin=str(lid))
            on.save()
            return HttpResponse("<script>alert('success !');window.location='/freelancer/freelancerhome/'</script>")
            # return HttpResponse("<div>progress-bar progress-bar-striped active</div>")
        else:
            return  render(request,"freelance/sendcomplaint.html")
    return login1(request)

def postedserv(request):
    if request.session['lin'] == "l":
        s = requiredservice.objects.filter(status="pending")
        return render(request, "freelance/postsearch.html" ,{'p':s})
    return login1(request)

# def postsearch(request):
#             search_key = request.POST['textfield']
#             s = requiredservice.objects.filter(service=search_key) | requiredservice.objects.filter(clogin__cname=search_key)
#             return render(request, "freelance/postsearch.html", {'p': s})
def saccept(request,id):
    if request.session['lin'] == "l":
        ob = requiredservice.objects.filter(id=id)
        o=requiredservicestat()
        o1=freelancers.objects.get(flogin=request.session['lid'])
        o.flogin=o1
        ob2 = requiredservice.objects.get(id=id)
        o.rsid=ob2
        o.save()
        ob.update(status="accepted")
        return HttpResponse("accepted", {'p': id})
    return login1(request)

def servu(request):
    if request.session['lin'] == "l":
         obj=freelancers.objects.get(flogin=request.session['lid'])
         ob = service.objects.filter(flogin=obj)
         return render(request, "freelance/serviceupost.html", {'p': ob})
    return login1(request)

def servremove(request,id):
    if request.session['lin'] == "l":
         c=service.objects.get(id=id)
         c.delete()
         return servu(request)
    return login1(request)
#client

def clienthome(request):
    if request.session['lin'] == "l":
        return  render(request,"client/clienthome.html")
    return login1(request)

#def updateprofile(request):
 #   return render(request,"client/update profile.html")

def profileup(request):
    if request.session['lin'] == "l":
        if request.method == "POST":
            ob = client.objects.get(clogin=request.session['lid'])
            a = request.POST['textfield']
            b = request.POST['textfield2']
            c = request.POST['textfield3']
            d = request.POST['textfield4']
            e = request.POST['textfield5']
            i = request.FILES['fileField']

            f = FileSystemStorage()
            cname = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            f.save(r"C:\Users\hp\PycharmProjects\freelance_marketplace\freelancer\static\\" + cname + ".jpg", i)
            path = "/static/" + cname + ".jpg"
            obj = client()
            obj.cname = a
            obj.cplace = b
            obj.cpin = c
            obj.cemail = d
            obj.cphone = e
            obj.cphoto = str(path)
            obj.id = ob.id
            obj.clogin = ob.clogin
            obj.save()
            return HttpResponse("<script>alert('Profile Updated');window.location='/freelancer/clienthome/'</script>")
        else:
            obj = client.objects.get(clogin=request.session['lid'])
            return render(request, "client/update profile.html", {'d': obj})
    return login1(request)




def  vifreelancer(request):
    if request.session['lin'] == "l":
        ob = freelancers.objects.filter()                        #select_related("fclientid")
        return render(request,"client/viewfreelancerprofile.html",{'p':ob})
    return login1(request)

def vifreelancermore(request,id):
    if request.session['lin'] == "l":
        ob=freelancers.objects.get(id=id)
        return render(request,"client/viewmorefreelancerprofile.html",{'p':ob})
    return login1(request)

def vfservice(request,id):
    if request.session['lin'] == "l":
        # ob1=freelancers.objects.get(id=id)
        ob=service.objects.filter(flogin=id)
        return render(request,"client/freelancer service.html",{'p':ob})
    return login1(request)

def sentorder(request,id):
    if request.session['lin'] == "l":
        ob=service.objects.get(id=id)
        o=client.objects.get(clogin=request.session['lid'])
        s=service_request()
        s.cdate=datetime.datetime.now().strftime("%Y-%m-%d")
        s.status='pending'
        s.clogin=o
        s.serviceid=ob
        s.save()
        return HttpResponse('<script>alert("order placed successfully");window.location="/freelancer/vifreelancer"</script>')
    return login1(request)


def ffeed(request,id):
    if request.session['lin'] == "l":
        ob = connection.cursor()
        ob.execute("select * from freelancer_feedback,freelancer_service_request,freelancer_service,freelancer_freelancers,freelancer_client where freelancer_feedback.serreqid_id=freelancer_service_request.id and freelancer_service_request.serviceid_id=freelancer_service.id and freelancer_service.flogin_id=freelancer_freelancers.id and freelancer_service_request.clogin_id=freelancer_client.id and freelancer_freelancers.id='"+str(id)+"'")
        ob1 = ob.fetchall() #freelancer_client.id=freelancer_feedback.fclientid_id
        return render(request,"client/feedback.html", {'p': ob1})
    return login1(request)


def viewnotif(request):
    if request.session['lin'] == "l":
        print(request.session['lid'])
        op=client.objects.get(clogin=request.session['lid'])
        ob = notification.objects.filter(nclientid=op)
        return render(request,"client/notifications.html",{'p':ob})
    return login1(request)



def replys(request):
    if request.session['lin'] == "l":
        print(request.session['lid'])
        op = client.objects.get(clogin=request.session['lid'])
        ob = ccomplaint.objects.filter(clogin=op)
        return render(request,"client/replys.html",{'p':ob})
    return login1(request)

def orderstatus(request):
    if request.session['lin'] == "l":
        e= connection.cursor()
        e.execute("select * from freelancer_service_request,freelancer_freelancers,freelancer_service,freelancer_client where freelancer_service_request.serviceid_id=freelancer_service.id and freelancer_service_request.clogin_id=freelancer_client.id and freelancer_client.clogin_id='"+str(request.session['lid'])+"' and freelancer_service.flogin_id=freelancer_freelancers.id")
        e1=e.fetchall()
        return render(request,"client/order status.html",{'p':e1})
    return login1(request)

def fb(request,id):
    if request.session['lin'] == "l":
        if request.method == 'POST':
            f=request.POST['textarea']
            d=datetime.datetime.now()#.strftime("%YYYY-%MM-%DD")
            obj=feedback()
            obj.feedback=f
            obj.feedback_date=d
            ob=service_request.objects.get(id=id)
            obj.serreqid=ob
            obj.save()
            return HttpResponse('<script>alert("feedback sent successfully");window.location="/freelancer/status/"</script>')

        else:
            return render(request,"client/give feedback.html",{'sid':id})
    return login1(request)

def pay(request,id,idd):
    if request.session['lin'] == "l":
         if request.method == 'POST':
                    #ob = client.objects.get(clogin=request.session['lid'])
                    a = request.POST['textfield']
                    b = request.POST['textfield2']
                    c = request.POST['textfield3']
                    d = request.POST['textfield4']

                    obj = bank.objects.filter(account=b,ifsc_code=c)   #(clogin=ob.id)
                    mb=obj[0].mainbalance
                    if int(mb)>int(d):
                        bl=int(mb)-int(d)
                        obj.update(mainbalance=str(bl))
                        obl=service_request.objects.filter(id=id)
                        obl.update(status="paid")
                        return HttpResponse("payed")
                    else:
                        # return HttpResponse("insufficient balance in your a/c...!!!!")
                        return HttpResponse("<script>alert('insufficient balance in your a/c...!!!!');</script>")
         else:
              return render(request, "client/bank.html", {'p':id,'pr':idd})
    return login1(request)

def scomplaint(request):
    if request.session['lin'] == "l":

        if request.method=="POST":

            comp=request.POST['textarea']
            print(comp)
            import datetime
            date=datetime.datetime.now()
            # lid=request.session['lid']
            on=ccomplaint()
            on.complaint=comp
            on.cdate=date
            on.replay='pending'
            on.replaydate=date
            on.clogin=client.objects.get(clogin=str(request.session['lid']))
            on.save()
            return HttpResponse("<script>alert('Complaint Sent');window.location='/freelancer/clienthome/'</script>")
        else:
            return  render(request,"client/csendcomplaint.html")
    return login1(request)

def logout(request):
    request.session['lin'] = ""
    return login1(request)


def services(request):
    if request.session['lin'] == "l":
        return render(request,"client/service.html")
    return login1(request)

def search(request):
    if request.session['lin'] == "l":
        search_key=request.POST['textfield']
        serv=service.objects.filter(service=search_key)|service.objects.filter(flogin__fname=search_key)
        return render(request,"client/service.html",{'p':serv})
    return login1(request)

def rserv(request):
    if request.session['lin'] == "l":

        return render(request,"client/reqserv.html")
    return login1(request)

def rspost(request):
    if request.session['lin'] == "l":
        try:
            t = request.POST['textfield']
            obj = requiredservice()
            obj.service = t
            obj.status="pending"
            obj.clogin=client.objects.get(clogin=request.session['lid'])
            obj.save()
            return clienthome(request)
        except Exception as e:
            print(e)
    return login1(request)


def reqstat(request):
    if request.session['lin'] == "l":
        e = connection.cursor()
        e.execute("select * from freelancer_requiredservice,freelancer_requiredservicestat,freelancer_freelancers,freelancer_client where freelancer_requiredservicestat.rsid_id=freelancer_requiredservice.id and freelancer_requiredservice.clogin_id=freelancer_client.id and freelancer_client.clogin_id='" + str(request.session['lid']) + "' and freelancer_requiredservicestat.flogin_id=freelancer_freelancers.id and freelancer_requiredservice.status='accepted'")
        e1 = e.fetchall()
        return render(request, "client/reqstat.html", {'p': e1})
    return login1(request)

#     ob = fcomplaint.objects.filter()
#     return render(request,"client/complaint to admin.html",{'p':ob})




def collegechat(request,id):
    if request.session['lin'] == "l":
        e = connection.cursor()
        e.execute("select flogin_id from freelancer_freelancers where id='"+id+"'")
        e1 = e.fetchone()
        request.session['fid']=e1[0]
        return render(request,"chatwithcolleges.html",{'did':request.session["lid"]})
    return login1(request)

def chatview(request):
    if request.session['lin'] == "l":
        # print("hai",request.session['fid'])
        from django.db.models import Q
        # da = college.objects.filter(~Q(LOGIN_id=request.session["loginid"]))
        da = freelancers.objects.filter(flogin= request.session['fid'])
        res = []
        for i in da:
            s = {'id': i.pk, 'name': i.fname, 'email': i.femail,'image':i.fphoto}
            # s = {'id': i.LOGIN_id, 'name': i.name, 'email': i.email,'image':i.image}
            res.append(s)
        # print(res,"kkkkkkkkkkkkkkkkkkk")
        return JsonResponse({'status': 'ok', 'data': res})
    return login1(request)

def clviewmsg(request,rid):
    if request.session['lin'] == "l":
        d = freelancers.objects.get(flogin= request.session['fid'])
        # g=college.objects.get(LOGIN=request.session["loginid"])
        g=client.objects.get(clogin=request.session["lid"])
        # print(str(g.id),str(rid),"kkkkkkkkkkkkkkkk")
        # obj = chat.objects.filter(COLLEGE_FROM_id=g.id,TO_COLLEGE_id=rid)
        obj = chat1.objects.filter(sender=request.session["lid"],receiver=request.session['fid'])|chat1.objects.filter(receiver=request.session["lid"],sender=request.session['fid'])

        res = []
        for i in obj:
            s = {'id':i.pk,'msg':i.message,'type':i.sender}
            res.append(s)
        # print(res,"555555555555555555")
        return JsonResponse({'status': 'ok', 'data': res,'name':d.fname,'image':d.fphoto,'sid':g.id})
    return login1(request)

def doctor_insert_chat(request,receiverid,msg):
    if request.session['lin'] == "l":

        import datetime
        datetime.date.today()  # Returns 2018-01-15
        showtime=datetime.datetime.now()
        obj=chat1()
        obj.message=msg
        obj.sender=request.session["lid"]
        obj.receiver=request.session["fid"]
        obj.chat_date=showtime
        obj.save()
        return JsonResponse({'status': 'ok'})
    return login1(request)


def collegechat1(request):
    if request.session['lin'] == "l":
        return render(request,"chatwithcolleges1.html",{'did':request.session["lid"]})
    return login1(request)

def chatview1(request):
    if request.session['lin'] == "l":
        e = connection.cursor()
        e.execute("select freelancer_client.clogin_id,freelancer_client.cname,freelancer_client.cemail,freelancer_client.cphoto from freelancer_chat1,freelancer_client where clogin_id=sender and receiver='"+str(request.session["lid"])+"' group by sender order by chat_date desc")
        e1 = e.fetchall()
        res = []
        for i in e1:
            s = {'id': i[0], 'name': i[1], 'email': i[2],'image':i[3]}
            res.append(s)
        return JsonResponse({'status': 'ok', 'data': res})
    return login1(request)

def clviewmsg1(request,rid):
    if request.session['lin'] == "l":
        print(rid)
        d = client.objects.get(clogin= rid)
        # g=college.objects.get(LOGIN=request.session["loginid"])
        g=freelancers.objects.get(flogin=request.session["lid"])
        # print(str(g.id),str(rid),"kkkkkkkkkkkkkkkk")
        # obj = chat.objects.filter(COLLEGE_FROM_id=g.id,TO_COLLEGE_id=rid)
        obj = chat1.objects.filter(sender=request.session["lid"],receiver=rid)|chat1.objects.filter(receiver=request.session["lid"],sender=rid)

        res = []
        for i in obj:
            s = {'id':i.pk,'msg':i.message,'type':i.sender}
            res.append(s)
        # print(res,"555555555555555555")
        return JsonResponse({'status': 'ok', 'data': res,'name':d.cname,'image':d.cphoto,'sid':g.id})
    return login1(request)

def doctor_insert_chat1(request,receiverid,msg):
    if request.session['lin'] == "l":

        import datetime
        datetime.date.today()  # Returns 2018-01-15
        showtime=datetime.datetime.now()
        obj=chat1()
        obj.message=msg
        obj.sender=request.session["lid"]
        obj.receiver=receiverid
        obj.chat_date=showtime
        obj.save()
        return JsonResponse({'status': 'ok'})
    return login1(request)

def rpu(request):
    if request.session['lin'] == "l":
         obj=client.objects.get(clogin=request.session['lid'])
         ob = requiredservice.objects.filter(clogin=obj)
         return render(request, "client/ureqserv.html", {'p': ob})
    return login1(request)

def postremove(request,id):
    if request.session['lin'] == "l":
         c=requiredservice.objects.get(id=id)
         c.delete()
         return rpu(request)
    return login1(request)