from django import forms

class StrdisplayForm(forms.Form):
    textinput = forms.CharField(label="inter text please", max_length=512)
