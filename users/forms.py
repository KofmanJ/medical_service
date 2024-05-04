from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms.widgets import SelectDateWidget

from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """ Класс создания формы регистрации """

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    """ Класс формы для редактирования профиля """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'patronymic', 'birth_date', 'avatar', 'phone')
        widgets = {
            'birth_date': forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': 'дд.мм.гггг'},
                                                 years=range(2024, 1924, -1)),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
