from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from captcha.fields import CaptchaField


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(), label="Подвердите пароль"
    )
    captcha = CaptchaField(label="Пройдите проверку, что вы не робот.")

    class Meta:
        model = CustomUser
        fields = (
            CustomUser.username.field.name,
            CustomUser.email.field.name,
            CustomUser.password.field.name,
        )
        labels = {
            CustomUser.username.field.name: "Никнэйм",
            CustomUser.email.field.name: "E-mail",
            CustomUser.password.field.name: "Пароль",
        }

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")
        username = cleaned_data.get("username")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Пароли не совпадают")
        if CustomUser.objects.filter(email=email):
            self.add_error(
                CustomUser.email.field.name,
                "Пользователь с таким email уже существует, попробуйте войти в аккаунт.",
            )
        if CustomUser.objects.filter(username=username):
            self.add_error(
                CustomUser.username.field.name,
                "Пользователь с таким ником уже существует, придумайте новый никнэйм.",
            )
        return cleaned_data

    def register(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")
        CustomUser.objects.create_user(
            username=username, email=email, password=password
        )


class Profile(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "avatar",
            "birthday",
            "mobile",
            "description",
        )
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }
