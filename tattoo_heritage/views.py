from django.shortcuts import render

from tattoo import settings
from .models import Artist
from .forms import *
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from tattoo_heritage.models import Artist


# Create your views here.
def index(request):
    index_page = loader.get_template("index.html")
    context = {}
    result1 = gallery1.objects.all()
    res_artist = Artist.objects.all()
    context["gal1_img"] = result1
    context["art"] = res_artist
    if request.method == 'POST':
        name = str(request.POST.get('uname'))
        semail = str(request.POST.get('uemail'))
        msg = request.POST.get('umsg')
        ph = request.POST.get('uph')
        send_mail(semail, msg, settings.EMAIL_HOST_USER,
                  ['collegeworks2019@gmail.com'], fail_silently=False)
        context["success_msg"] = "Sucessfully send"
        return HttpResponse(index_page.render(context, request))
    return HttpResponse(index_page.render(context, request))


def view_work(request):
    if request.method == 'POST':
        art_id = request.POST.get('ar_id')
        art_work = artist_work.objects.filter(a_id=art_id)
        return render(request, 'View_Work.html', {'artist_work': art_work})
    return render(request, 'View_Work.html')


@login_required
def disp_artist(request):
    result_disp = Artist.objects.order_by("a_name")
    if request.method == 'POST':
        i_a_id = request.POST.get('picid')
        Artist.objects.filter(a_id=i_a_id).delete()
    return render(request, 'disp_artist.html', {'artist': result_disp})


@login_required
def add_artist(request):
    if request.method == 'POST':
        form = AddArtist_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'addArtist.html', {'sucess_msg': 'Sucessfully added', 'form': form})
    else:
        form = AddArtist_Form
        return render(request, 'addArtist.html', {'form': form})


@login_required
def add_gal1(request):
    if request.method == 'POST':
        form1 = Addimggal1_Form(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return render(request, "gal1.html", {'sucess_msg': 'Sucessfully added', 'form': form1})
        else:
            form1 = Addimggal1_Form
            return render(request, 'gal1.html', {'fail_msg': 'Failed to add', 'form': form1})
    else:
        form1 = Addimggal1_Form
        return render(request, 'gal1.html', {'form': form1})

@login_required
def add_work(request):
    if request.method == 'POST':
        form5 = AddWork_form(request.POST, request.FILES)
        if form5.is_valid():
            form5.save()
            return render(request, 'addWork.html', {'sucess_msg': 'Sucessfully added', 'form': form5})
    else:
        form5 = AddWork_form
        return render(request, 'addWork.html', {'form': form5})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return render(request, 'disp_artist.html')
        else:
            fail = {'wrong': 'Invalid Username or Password'}
            return render(request, 'login.html', context=fail)
    return render(request, 'login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def del_gal(request):
    res_disp = gallery1.objects.all()
    if request.method == 'POST':
        img_id = request.POST.get('img_id')
        gallery1.objects.filter(g1_id=img_id).delete()
        return render(request, 'disp_gal.html', {'gal': res_disp})
    return render(request, 'disp_gal.html',{'gal': res_disp})


@login_required
def del_work(request):
    res_disp = artist_work.objects.all()
    if request.method == 'POST':
        im_id = request.POST.get('im_id')
        artist_work.objects.filter(w_id = im_id).delete()
        return render(request, 'disp_work.html', {'work':res_disp})
    return render(request, 'disp_work.html', {'work': res_disp})

@login_required
def update_artist(request):
    if request.method == 'POST':
        a_id = request.POST.get('id')
        a_name = request.POST.get('name')
        a_img = request.FILES.get('imgf')
        a_contact = request.POST.get('contact')
        a_email = request.POST.get('email')
        a_des = request.POST.get('des')
        a_fb = request.POST.get('fb')
        a_insta = request.POST.get('insta')
        a = Artist.objects.get(a_id = a_id)
        a.a_name = a_name
        a.a_img = a_img
        a.a_contact = a_contact
        a.a_email = a_email
        a.a_des = a_des
        a.a_fb = a_fb
        a.a_insta = a_insta
        a.save()
        # Artist.objects.filter(a_id=a_id).update(a_name= a_name, a_img= a_img, a_contact=a_contact, a_email=a_email,
        #                 a_des=a_des, a_fb=a_fb, a_insta=a_insta)

        return render(request, 'disp_artist.html')
    return render(request, 'disp_artist.html')





