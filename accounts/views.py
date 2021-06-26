from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import  UserLoginForm,RegisterUserForm,UpdateUserForm
from django.contrib import messages

def login_view(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request,email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Вход выполнен успешно')
            return redirect('home')

    return render (request,'accounts/login.html',{'form':form})

def register_view(request):

    form=RegisterUserForm(request.POST,request.FILES or None)
    if form.is_valid():
        data=form.cleaned_data
        User=get_user_model()
        del data['password2']
        data['password']=data['password1']
        del data['password1']
        new_user=User(**data)
        new_user.set_password(new_user.password)#Хеширование пароля
        new_user.save()
        return redirect('home')
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return  redirect('home')

def update_view(request,slug,pk):
    user = request.user #Пользователь системы
    if user.is_authenticated:
        if  f'{user.slug}-{user.pk}'==f'{slug}-{pk}': #Если обновляет данные действительный пользователь
            if request.method=='POST' or request.method=='FILES':
                form=UpdateUserForm(request.POST,request.FILES)
                if form.is_valid():
                    data=form.cleaned_data
                    user=get_user_model().objects.get(email=user.email)
                    if data.get('name'):
                        user.name=data.get('name')
                    if data.get('logo'):
                        user.logo=data.get('logo')
                    if data.get('old_password') and data.get('password'):
                        if check_password(data.get('old_password'),user.password):
                            print('abc',user.password)
                            user.password = data.get('password')
                            user.set_password(user.password) #Функкция шифрования пароля

                    user.save()
                    messages.success(request, 'Данные обновлены')
                    return redirect('update',slug=slug,pk=pk)
            else:
                form=UpdateUserForm(initial={'name':user.name,'logo':user.logo})
                return render(request,'accounts/update.html',{'form':form})
        else:
            return redirect('update', slug=user.slug, pk=user.pk)
    else:

        return redirect('login')

def personal_cabinet_view(request,slug,pk):
    user=request.user
    if f'{user.slug}-{user.pk}' != f'{slug}-{pk}':
        return redirect('personal_cabinet', slug=user.slug, pk=user.pk)
    return render(request,'accounts/personal_cabinet.html',{})


