from django.db import models

# Create your models here.



class login(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    types = models.CharField(max_length=500)

class  client(models.Model):
    clogin = models.ForeignKey(login,default=1,on_delete=models.CASCADE)
    cname = models.CharField(max_length=500)
    cplace = models.CharField(max_length=500)
    cpin = models.CharField(max_length=500)
    cemail = models.CharField(max_length=500)
    cphone = models.BigIntegerField()
    cphoto = models.CharField(max_length=500)

class freelancers(models.Model):
    flogin = models.ForeignKey(login, default=1, on_delete=models.CASCADE)
    fname = models.CharField(max_length=500)
    fplace = models.CharField(max_length=500)
    fpost = models.CharField(max_length=500)
    fpin = models.IntegerField()
    femail = models.CharField(max_length=500)
    fcontact = models.CharField(max_length=500)
    fexperiance = models.CharField(max_length=500)
    fphoto = models.CharField(max_length=500)
    skill=models.CharField(max_length=500)

class notification(models.Model):
    to=models.CharField(max_length=500)
    notification = models.CharField(max_length=500)
    ndate = models.DateField()
    # nfreelancerid = models.ForeignKey(freelancers, default=1, on_delete=models.CASCADE)
    nclientid = models.ForeignKey(client, default=1, on_delete=models.CASCADE)

class notification_f(models.Model):
    to=models.CharField(max_length=500)
    notification = models.CharField(max_length=500)
    ndate = models.DateField()
    nfreelancerid = models.ForeignKey(freelancers, default=1, on_delete=models.CASCADE)
    # nclientid = models.ForeignKey(client, default=1, on_delete=models.CASCADE)

class fcomplaint(models.Model):
    fl_loginid = models.ForeignKey(freelancers, default=1, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=500)
    cdate= models.DateField()
    replay = models.CharField(max_length=500)
    replaydate = models.DateField()

class ccomplaint(models.Model):
    clogin = models.ForeignKey(client, default=1, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=500)
    cdate = models.DateField()
    replay = models.CharField(max_length=500)
    replaydate = models.DateField()

class service(models.Model):
    flogin = models.ForeignKey(freelancers, default=1, on_delete=models.CASCADE)
    service = models.CharField(max_length=500)
    service_details = models.CharField(max_length=500)
    price = models.CharField(max_length=500)

class service_request(models.Model):
    clogin = models.ForeignKey(client, default=1, on_delete=models.CASCADE)
    serviceid = models.ForeignKey(service, default=1, on_delete=models.CASCADE)
    cdate = models.DateField()
    status = models.CharField(max_length=500)

class feedback(models.Model):
    # fclientid = models.ForeignKey(client,default=1,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)
    feedback_date = models.DateField()
    serreqid = models.ForeignKey(service_request, default=1, on_delete=models.CASCADE)


class chat(models.Model):
    flogin = models.ForeignKey(login, default=1, on_delete=models.CASCADE)
    clogin = models.ForeignKey(client, default=1, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    chat_date = models.DateField()

class bank(models.Model):
     bankname = models.CharField(max_length=20)
     account = models.BigIntegerField()
     ifsc_code = models.CharField(max_length=20)
     mainbalance = models.BigIntegerField()
     #clogin = models.ForeignKey(client, default=1, on_delete=models.CASCADE)
     # requestid = models.ForeignKey(service_request, default=1, on_delete=models.CASCADE)


class requiredservice(models.Model):
    clogin = models.ForeignKey(client, default=1, on_delete=models.CASCADE)
    #flogin = models.ForeignKey(freelancers, default=1, on_delete=models.CASCADE)
    service = models.CharField(max_length=500)
    status = models.CharField(max_length=100)

class requiredservicestat(models.Model):
    rsid = models.ForeignKey(requiredservice, default=1, on_delete=models.CASCADE)
    flogin = models.ForeignKey(freelancers, default=1, on_delete=models.CASCADE)
    #service = models.CharField(max_length=500)
    #status = models.CharField(max_length=100)

#     ////////////////////////////////////////////////////////////////////////////
# class job(models.Model):
#     service_id = models.ForeignKey(service, default=1, on_delete=models.CASCADE)
#     client_details = models.CharField(max_length=500)
#     faddress = models.CharField(max_length=500)
#     clogin = models.ForeignKey(client, default=1, on_delete=models.CASCADE)
#     flogin = models.ForeignKey(login, default=1, on_delete=models.CASCADE)
#     status = models.CharField(max_length=500)
#
#
# class payment(models.Model):
#     job = models.ForeignKey(job, default=1, on_delete=models.CASCADE)
#     price = models.BigIntegerField()
#     payment_date = models.DateField()
#     status=models.CharField(max_length=200)
#
#
#

class chat1(models.Model):
    receiver = models.IntegerField()
    sender = models.IntegerField()
    message = models.CharField(max_length=500)
    chat_date = models.DateField()
