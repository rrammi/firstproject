from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'First Name'
            }
        )
    )

    last_name = forms.CharField(
        label='Enter Last Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Last Name'
            }
        )
    )
    user_name = forms.CharField(
        label="Enter User Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'User Name'
            }
        )
    )

    password = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
    email = forms.EmailField(
        label='Enter Your Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email ID'
            }
        )
    )
    number = forms.IntegerField(
        label="Enter Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Number'
            }
        )
    )



class LoginForm(forms.Form):
    user_name = forms.CharField(
        label="Enter User Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'User Name'
            }
        )
    )

    password = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )