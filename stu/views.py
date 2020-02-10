import math

from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import Student
from stu.models import ChainBehavior


def login(request):
    m = request.method
    if m == "GET":
        return render(request,'login.html')
    else:
        name = request.POST.get('uname','')
        print(name)
        pwd = request.POST.get('passwd','')
        print(pwd)

        if name and pwd:
            stu = Student(sname=name,spwd=pwd)
            stu.save()
            return HttpResponse('successs')
        return HttpResponse('fail')


def index(request):
    return render(request, 'login.html')


def show(request):
    stus = Student.objects.all()

    return render(request,'show.html',{'stus':stus})


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        uname = request.POST.get('uname','')
        pwd = request.POST.get('passwd','')

        print("000000000")
        print(uname)
        print(pwd)
        print('oooooooo')

        if uname and pwd:
            c = Student.objects.filter(sname=uname,spwd=pwd).count()

            print("000000000")
            print(uname)
            print(pwd)
            print(c)
            if c == 1:
                return HttpResponse('success login')

    return HttpResponse('failed to login')


def v(request):
    return render(request,'login.html')

def movie_01(request):
    num =  request.GET.get('num',1)
    n = int(num)
    movies = ChainBehavior.objects.all()
    pager = Paginator(movies,20)
    # perpage_data = pager.page(n)

    try:
        perpage_data = pager.page(n)
    except PageNotAnInteger:
        perpage_data = pager.page(1)
    except EmptyPage:
        perpage_data = pager.page(pager.num_pages)

    return render(request,'index.html',{'movies':perpage_data,'pager':pager})

def movie(request):
    num = request.GET.get('num',1)
    movies,num = page(num)

    pre_page = num - 1
    next_page = num + 1

    return render(request,'index.html',{"movies":movies,'prepages':pre_page,'nextpages':next_page})

def page(num,size=20):
    num = int(num)

    totalRecord = ChainBehavior.objects.count()


    totalPages = math.ceil(totalRecord*1.0/size)


    ##越界
    if num < 1:
        num = 1

    if num > totalPages:
        num = totalPages

    movies = ChainBehavior.objects.all()[(num-1)*size:(num*size)]
    return movies,num







