from django import forms

class ItemRegistForm(forms.Form):
    url = forms.CharField(label="URL")
    hope_price = forms.CharField(label="希望価格")