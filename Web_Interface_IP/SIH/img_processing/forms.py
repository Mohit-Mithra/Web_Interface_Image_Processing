from django import forms

class FileFieldForm(forms.Form):
    upload_files_here = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
