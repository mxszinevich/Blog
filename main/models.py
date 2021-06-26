from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models import SET_NULL
from config import settings
from slugify import slugify
from bs4 import BeautifulSoup

def generate_filename(instance, filename):
    name=BeautifulSoup(instance.name,'html.parser').text
    filename = f'article_image/{name[:25]}/{filename[:10]}.{filename.split(".")[-1]}'
    print(filename)
    return filename

class Article(models.Model):
    name = RichTextField()
    slug=models.SlugField(unique=True,verbose_name='Ссылка на статью')
    description=RichTextField(default='',blank=True)
    body= RichTextUploadingField()
    date_time=models.DateTimeField(auto_now_add=True,verbose_name='Время добавления')
    image=models.ImageField(upload_to=generate_filename,verbose_name='Изображение',blank=True,null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Пользователь',on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.name

    def save(self):
        name = BeautifulSoup(self.name, "html").text
        self.slug=slugify(f'{name[:30]}')
        super(Article, self).save()

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'



