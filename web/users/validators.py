from django.forms import ValidationError
import string
import phonenumbers


def validate_for_username(username):
    if username == "profile":
        raise ValidationError("Нельзя создать аккаунт с таким никнэймом.")
    for letter in username:
        if (
            letter not in string.ascii_letters
            and letter not in string.digits
            and letter not in "-_"
        ):
            raise ValidationError(
                "Никнэйм может состоять только из латинских букв и символов - и _"
            )


def validate_for_mobile(mobile):
    try:
        phonenumbers.parse(f"+{str(mobile)}")
    except Exception:
        raise ValidationError("Укажите правильный номер телефона.")
