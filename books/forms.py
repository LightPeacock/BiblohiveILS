# forms.py
from django import forms

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField()


class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search for a book')
