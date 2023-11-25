from django.forms import ModelForm, CharField, TextInput, DateInput, DateField
from .models import Tag, Author, Quote



class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']



class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_date = DateField(required=False, widget=DateInput())
    born_location = CharField(max_length=50, required=False, widget=TextInput())
    description = CharField(required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'description']
        exclude = ['born_date', 'born_location']




class QuoteForm(ModelForm):
    quote = CharField(min_length=10, max_length=500, required=True, widget=TextInput())
    tags = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    author = CharField(min_length=5, max_length=50, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote']
        exclude = ['tags', 'author'] # які поля моделі слід виключити з форми