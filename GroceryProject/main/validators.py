import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class UppercaseValidator(object):

    '''The password must contain at least 1 uppercase letter, A-Z.'''

    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("Пароль должен содержать как минимум 1 большую букву A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "В вашем пароле должно быть как минимум 1 большая буква, A-Z."
        )

class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("Пароль должен содержать как минимум 1 маленькую букву, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "В вашем пароле должно быть как минимум 1 маленькая буква, a-z."
        )

class PasswordsMatchValidator(object):
    def validate(self, password, password2, user=None):
        if password != password2:
            raise ValidationError(
                _("Пароли не совпадают."),
                code='passwords_do_not_match',
            )

    def get_help_text(self):
        return _(
            "Пароли не совпадают."
        )