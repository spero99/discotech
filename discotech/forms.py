from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    firstname = forms.CharField(label='firstname', max_length=100)
    lastname = forms.CharField(label='lastname', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    telephone = forms.CharField(label='telephone', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class TwofaForm(forms.Form):
    code = forms.Charfield(label='2fa', max_length=5)


class Transaction(forms.Form):
    #user info
    firstname = forms.CharField(label='firstname', max_length=100)
    lastname = forms.CharField(label='lastname', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    telephone = forms.CharField(label='telephone', max_length=100)
    #product info
    prod_id = forms.CharField(label='prod_id', max_length=100)
    name = forms.CharField(label='product', max_length=100)
    brand = forms.CharField(label='brand', max_length=100)
    price = forms.CharField(label='price', max_length=100)
    #card_info
    cardnumber = forms.CharField(label='cardnumber', max_length=100)
    cardcode = forms.CharField(label='cardcode', max_length=100)