from django import forms
def valid_for_a(svalue):
    if svalue[0].lower()=='a':
        raise forms.ValidationError('starting with a')
def valid_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError('len is lessthan 5')
class studentform(forms.Form):
    sname=forms.CharField(max_length=100,validators=[valid_for_a,valid_for_len])
    sage=forms.IntegerField()
    email=forms.EmailField(validators=[valid_for_a])
