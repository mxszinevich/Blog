from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from slugify import slugify

class MyUserManager(BaseUserManager):
    def create_user(self, email,slug,name,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('У пользователей должен быть адрес электронной почты')
        if not name:
            raise ValueError('У пользователей должно быть имя')

        user = self.model(email=self.normalize_email(email),name=name,slug=slug)

        user.set_password(password)# Хеширование пароля
        user.save(using=self._db)
        return user

    def create_superuser(self, email,slug, name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            slug=slug
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,

    )
    slug=models.SlugField(unique=True, verbose_name='Ссылка на пользователя')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False,verbose_name='Администратор')
    name= models.CharField(max_length=100,verbose_name="Имя пользоватея")
    logo=models.ImageField(upload_to='user_logo/',verbose_name='Логотип')
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    class Meta:
        verbose_name='пользователь'
        verbose_name_plural='пользователи'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self,*args, ** kwargs):
        if not self.slug:
            self.slug=slugify(f'{self.name}-{self.email.split("@")[0]}')
        super().save(*args, **kwargs)