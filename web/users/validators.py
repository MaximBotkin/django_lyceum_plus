import string

import phonenumbers
from django.forms import ValidationError


def validate_for_username(username):
    if username == "profile":
        raise ValidationError("Нельзя создать аккаунт с таким никнэймом.")
    nedded_symbols = f'{string.ascii_letters}{string.digits}-_'
    for letter in username:
        if letter not in nedded_symbols:
            raise ValidationError(
                "Никнэйм может состоять только из латинских букв и символов - и _"
            )


def validate_for_mobile(mobile):
    try:
        phonenumbers.parse(f"+{str(mobile)}")
    except Exception:
        raise ValidationError("Укажите правильный номер телефона.")
