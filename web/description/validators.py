from django.forms import ValidationError
from django.utils.deconstruct import deconstructible
from re import match


@deconstructible
class RegexValidator:
    message = "Убедитесь, что вы ввели цвет в HEX формате (сейчас %(show_value)s)."
    code = "must_hex"

    def __init__(self, limit_value):
        self.limit_value = limit_value

    def __call__(self, value):
        try:
            val = value.html
        except Exception:
            val = value
        group = match(self.limit_value, val)
        params = {"limit_value": self.limit_value, "show_value": val, "value": value}
        if not group or group[0] != val:
            raise ValidationError(self.message, code=self.code, params=params)
