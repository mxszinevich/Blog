from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms



class ArticleForm(forms.Form):
    name=forms.CharField(label='Название статьи',widget=CKEditorWidget(config_name='awesome_ckeditor'))
    description = forms.CharField(label='Описание статьи', widget=CKEditorWidget(config_name='awesome_ckeditor'))
    image=forms.ImageField(label='Изображение статьи',widget=forms.FileInput(attrs={'class':' form-control'}),required=False)

    body=forms.CharField(label='Содержание статьи',widget=CKEditorUploadingWidget(attrs={
                                           'data-field': 'abc_description',
                                           "class": "form-control abc_description",
                                           'placeholder': 'ABC Description'}))
    publication_status=forms.BooleanField(label='Опубликовано',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),required=False)

    """
    def clean(self):
        
        data=self.cleaned_data
        if not data.get('name'):
            raise forms.ValidationError('Заполните имя статьи')

        return self.cleaned_data
    """
            


