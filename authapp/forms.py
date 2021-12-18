from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import ShopUser
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    error_css_class = 'has-error'

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MoscowStoppersMixin:
    def city_block(self):
        data = self.cleaned_data['city']
        if data.lower() == ("moscow" or "москва"):
            raise forms.ValidationError("Не для жителей Москвы!")
        return data

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data


class ShopUserEditForm(MoscowStoppersMixin, UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'city', 'phone_number', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class ShopUserRegisterForm(MoscowStoppersMixin, UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'city', 'phone_number')

    error_css_class = 'has-error'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

