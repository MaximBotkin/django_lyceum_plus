from django.forms import ValidationError
import string


def validate_for_username(username):
    for letter in username:
        if letter not in string.ascii_letters and \
                letter not in string.digits and letter not in '-_':
            raise ValidationError(
                'Никнэйм может состоять только из латинских букв и символов - и _'
            )
