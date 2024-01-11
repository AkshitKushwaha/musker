from django import forms
from .models import Meep
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MeepForm(forms.ModelForm):
    body = forms.CharField(required=True, widget = forms.widgets.Textarea(
        attrs={
            "placeholder": "Meep Something!",
            "class": "form-control",
        }
    ),
    label = "",
    )

    class Meta:
        model = Meep
        exclude = ("user",)



class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "", widget=forms.widgets.TextInput(
        attrs={
            "placeholder": "Email Address",
            "class": "form-control",
        }
    ))

    first_name = forms.CharField(label = "", max_length = 100, widget=forms.widgets.TextInput(attrs={
        "placeholder": "First Name",
        "class": "form-control",
    }))

    last_name = forms.CharField(label = "", max_length = 100, widget=forms.widgets.TextInput(attrs={
        "placeholder": "Last Name",
        "class": "form-control",
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'







#note:-
        
#In Django, the exclude option in a ModelForm is used to specify fields that should not be included in the form.

#In your code, exclude = ("user",) means that the user field from the Meep model will not be included in the MeepForm. This is useful when you want to manually handle a field instead of letting the form automatically generate it.

#or example, you might want to automatically set the user field to the currently logged-in user in your view or controller, rather than letting the user choose a value for this field in the form.