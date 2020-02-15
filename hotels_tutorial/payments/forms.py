from django import forms
from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birthday', 'email', 'gender', 'phone']

    def clean(self):
        super(PersonForm, self).clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        birthday = self.cleaned_data.get('birthday')
        email = self.cleaned_data.get('email')
        gender = self.cleaned_data.get('gender')
        phone = self.cleaned_data.get('phone')

        if not first_name or not last_name or not birthday or not email or not gender or not phone:
            raise forms.ValidationError('something missing')

        return self.cleaned_data


