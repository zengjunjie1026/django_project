from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decoraters import *

# Create your views here.


def contact(request):
    return HttpResponse('contact page')


def admin(request):
    return None


@login_required(login_url='login')
def products(request):
    product = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': product})


@login_required(login_url='login')
def customers(request, pk):
    customer = Customers.objects.get(id=pk)
    orders = customer.order_set.all()

    total_count = orders.count()
    pending_count = orders.filter(status='pending')
    myFilter = OrderFilter(request.GET, queryset=orders)

    order = myFilter.qs
    print(order)

    context = {'customer': customer, 'orders': order, 'total_count': total_count,
               'myFilter': myFilter}

    return render(request, 'accounts/customers.html', context)



@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin','staff','customers'])
def home(request):
    orders = Order.objects.all()
    customers = Customers.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status='delivered').count()
    pending = orders.filter(status='pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'pending': pending,
               'delivered': delivered}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customers, Order, fields=('product', 'status', 'note'), extra=10)
    customer = Customers.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer':customer})

    if request.method == 'POST':
        # print("pppppp",request.POST)
        # form = OrderForm(request.POST)

        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/accounts/')

    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        # print("pppppp",request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/accounts/')

    context = {"form": form}
    return render(request, 'accounts/update_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/accounts/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'scuessful create {} '.format(user))
            return redirect('/accounts/login/')
    context = {'form':form}
    return render(request,"accounts/register.html",context)


@unauthenthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'password or username not correct!')
            return render(request, "accounts/login.html")
    return render(request, "accounts/login.html")


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url = '/accounts/login')
@allowed_users(allowed_roles=['admin'])
def user(request):
    # user = request.GET.get(User)

    orders = request.user.customers.order_set.all()
    total_orders = orders.count()

    delivered_count = orders.filter(status='delivered')
    pending_count = orders.filter(status='pending')

    context = {'orders':orders,'total_count':total_orders,'delivered_count':delivered_count,
               'pending_count':pending_count}
    return render(request,'accounts/user.html',context)



@login_required(login_url='login')
def accountSetting(request):
    customer = request.user.customers
    form = CustomersForm(instance=customer)
    if request.method == "POST":
        form = CustomersForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            print('ooooo')
            form.save()
    context = {'form':form}
    return render(request,'accounts/account_seeting.html',context)