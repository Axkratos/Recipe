from django.shortcuts import render, get_object_or_404, redirect
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        if receipe_name and receipe_description and receipe_image:
            Receipe.objects.create(
                receipe_image=receipe_image,
                receipe_name=receipe_name,
                receipe_description=receipe_description
            )
            return redirect('receipes')

    search_query = request.GET.get('search', '')
    if search_query:
        queryset = Receipe.objects.filter(receipe_name__icontains=search_query)
    else:
        queryset = Receipe.objects.all()

    context = {'receipes': queryset, 'search_query': search_query}
    return render(request, 'recipes.html', context)

def upload_receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        if receipe_name and receipe_description and receipe_image:
            Receipe.objects.create(
                receipe_image=receipe_image,
                receipe_name=receipe_name,
                receipe_description=receipe_description
            )
            return redirect('receipes')

    return render(request, 'upload.html')

def delete_receipe(request, id):
    queryset = get_object_or_404(Receipe, id=id)
    queryset.delete()
    return redirect('receipes')

def update_receipe(request, id):
    queryset = get_object_or_404(Receipe, id=id)

    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('receipes')

    context = {'receipe': queryset}
    return render(request, 'updatereceipes.html', context)



def login_page(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'User doesnot exists')
            return redirect('/register')
        user =authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid Credentials')
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/')
    return render(request,'login.html')



def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'Username already exists')
            return render(request, 'register.html', {'error_message': 'Username already exists'})

        user = User.objects.create(
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save()
        print(user.username)

        return redirect('/login')

    return render(request, 'register.html')

def logout_page(request):
    logout(request)