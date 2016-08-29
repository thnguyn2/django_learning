from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    #Define different fields of the form
    name = forms.CharField(max_length=128, help_text="Please enter the category name")
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    class Meta:
        #Provide connection between the ModelForm and model
        model=Category
        fields = ('name',)
        #Which field to be visible in our form, needs to be a tuple here

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page")
    url = forms.URLField(max_length=128, help_text="Please enter the URL of the page")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    #def clean(self):
    #    clean_data = self.cleaned_data
    #    url = clean_data.get('url')
    #    if url and not url.startswiths('http://'):
    #        url = 'http://'+url
    #        clean_data['url']=url
    #    return clean_data


    class Meta:
        model = Page
        #Associate the ModelForm with the Page model
        exclude = ('category',)

        #Note that category here is a field, defined in models.py
        #Equivalent to fields = ('title','url','views',)



