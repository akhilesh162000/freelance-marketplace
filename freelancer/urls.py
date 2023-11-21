from django.urls import path

from . import views
from django.conf.urls.static import static

from freelance_marketplace import settings

urlpatterns = (
    path('login/', views.login1, name="login"),
    path('logpost/', views.logpost, name="login"),
path('forgot/', views.forgot),
    path('adminhome/', views.adminhome),
    path('', views.homepage),
    path('vclient/', views.viewclients),
    path('vclient_more/<int:id>', views.viewclients_more),
    path('vfreelancers/', views.viewfreelancers),
    path('vfreelancer_more/<int:id>', views.viewfreelancers_more),
    path('vfeedbacks/<int:id>', views.feedbacks),
    path('voservice/<int:id>', views.offeredservice),
    path('snotifications/', views.sendnot),

    path('notifpost/<id>', views.notifpost),
    path('notifpost1/<id>', views.notifpost1),
    path('vfcomps/', views.fcomplaints),
    path('freply/<id>', views.freplays),
    path('fcomppost/<id>', views.fcomppost),
    path('vccomps/', views.ccomplaints),
    path('creply/<id>', views.creplays),
    path('ccomppost/<id>', views.ccomppost),
    path('notif/', views.nto),
    path('sendnotif1/<id>', views.sendnotif1),
    path('sendnotif/<id>', views.sendnotif),
path('crs/<int:id>', views.crs),
    # freelasencer


    path('freelancerhome/', views.freelancerhome),
    # path('uprofile/',views.updateprof),
    path('profileupdate/', views.profileupdate),

    path('pservice/', views.postservices),
    path('servicepost/', views.servicepost),
    path('viclient/', views.viclients),
    path('vicmore/<int:id>', views.viclientsmore),
    path('vnotifications/', views.viewnot),
    path('vreply/', views.viewrep),

    path('fregister/', views.fregister),

    path('vfeed/', views.vfeed),
    # path('vfeed/', views.vfeed),
    path('vorder/', views.vorders),
    path('oaccept/<servicerid>', views.oaccept),
    path('oreject/<servicerid>', views.oreject),
    path('scomp/', views.scomp),
    path('pserv/', views.postedserv),
    path('accept/<id>', views.saccept),
    # path('oreject/<servicerid>', views.oreject),
    path('urserv/', views.servu),
    path('remove/<id>', views.servremove),
    # client

    path('logout/', views.logout),

    path('clienthome/', views.clienthome),
    path('register/', views.cregister),
    # path('upprofile/',views.updateprofile),
    path('profupdate/', views.profileup),
    path('sentorder/<int:id>', views.sentorder),
    path('vifreelancer/', views.vifreelancer),
    path('vifmore/<int:id>', views.vifreelancermore),
    path('vfservice/<int:id>', views.vfservice),
    path('ffeed/<int:id>', views.ffeed),
    path('vnot/', views.viewnotif),
    path('scomplaint/', views.scomplaint),
    path('replys/', views.replys),
    path('status/', views.orderstatus),
    path('feedback/<int:id>', views.fb),
    path('sendpayment/<int:id>/<int:idd>', views.pay),
    path('services/', views.services),
    path('search/', views.search),
    path('rserv/', views.rserv),
    path('rspost/', views.rspost),
    path('rstat/', views.reqstat),
    path('collegechat/<id>', views.collegechat),
    path('clviewmsg/<rid>', views.clviewmsg),
    path('doctor_insert_chat/<str:receiverid>/<str:msg>', views.doctor_insert_chat),
    path('chatview/', views.chatview),
    path('collegechat1/', views.collegechat1),
    path('clviewmsg1/<rid>', views.clviewmsg1),
    path('doctor_insert_chat1/<str:receiverid>/<str:msg>', views.doctor_insert_chat1),
    path('chatview1/', views.chatview1),
path('rpu/', views.rpu),
path('pr/<id>',views.postremove),
)

#urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)