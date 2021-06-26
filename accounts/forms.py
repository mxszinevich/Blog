from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

User=get_user_model()#Получаем текущую модель пользователя

class UserLoginForm(forms.Form):

    email=forms.CharField(label="Email",
                          widget=forms.EmailInput(
                              attrs={'class':'form-control',
                                     'placeholder':'name@example.com',
                                     'id_for_label':'email_id'
                                     }))

    password = forms.CharField(label="Пароль",
                            widget=forms.PasswordInput(
                                attrs={'class': 'form-control',

                                       'id_for_label': 'password_id'
                                       }))

    def clean(self):

        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            qs=User.objects.filter(email=email)

            if not qs.exists():#Если qs пустой
                raise forms.ValidationError('Такого пользователя нет')

            if not check_password(password,qs.first().password):
                raise forms.ValidationError('Неверный пароль')

            user = authenticate(email=email, password=password)

            if not user:
                raise forms.ValidationError('Аккаунт не действителен')


            return self.cleaned_data #Возвращаем данные только если они есть
        

class RegisterUserForm(forms.Form):
    email = forms.CharField(label="Email",
                            widget=forms.EmailInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'name@example.com',
                                       'id_for_label': 'email_id'
                                       }))
    name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-control','id_for_label': 'name_id'}))
    logo= forms.ImageField(label="Фото профиля", widget=forms.FileInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control','id_for_label': 'password1_id'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class': 'form-control','id_for_label': 'password2_id'}))

    def clean(self):
        data=self.cleaned_data
        email=data.get('email')
        if email:
            qs=User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError('Такой пользователь уже существует')

        return self.cleaned_data

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1!=password2:

            raise forms.ValidationError('Пароли не совпадают')

        return password2


class UpdateUserForm(forms.Form):

    name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-control','id_for_label': 'name_id'}),required=False)
    logo= forms.ImageField(label="Фото профиля", widget=forms.FileInput(attrs={'class':'form-control'}),required=False)
    old_password = forms.CharField(label="Введите старый пароль", widget=forms.PasswordInput(attrs={'class': 'form-control','id_for_label': 'password1_id'}),required=False)
    password = forms.CharField(label="Изменение пароля", widget=forms.PasswordInput(attrs={'class': 'form-control','id_for_label': 'password1_id'}),required=False)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class': 'form-control','id_for_label': 'password2_id'}),required=False)

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password!=password2:

            raise forms.ValidationError('Пароли не совпадают')

        return password2



