from django import forms

class BooksForms(forms.Form):
    title=forms.CharField()
    author=forms.CharField()
    published_date=forms.DateField()
    desc=forms.CharField(widget=forms.Textarea(attrs={
        'rows':15,
        'cols':35,

    }))

