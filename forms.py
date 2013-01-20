from django import forms

class DocumentForm(forms.Form):
    name = forms.CharField(max_length=50)
    type = forms.CharField(max_length=50)
    description = forms.CharField(max_length=3000)
    dayRentalPrice = forms.IntegerField()
    docfile = forms.FileField(
        label='Select an image',
        help_text='max. 42 megabytes'
    )
    user = forms.CharField(max_length=50)
    userEmail = forms.EmailField()

class RentForm(forms.Form):
    gear_id = forms.IntegerField()
    note = forms.CharField(max_length=3000, widget=forms.Textarea)
