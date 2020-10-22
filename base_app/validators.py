import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def iran_national_code_validator(_code):
    if not re.search(r"^\d{10}$", _code):
        raise ValidationError(
            _("The national code is invalid, it must be ten digits"),
        )

    check = int(_code[9])
    s = sum([int(_code[x]) * (10 - x) for x in range(9)]) % 11
    if (2 > s == check) or (s >= 2 and (check + s) == 11):
        pass
    else:
        raise ValidationError(
            _("The national code is invalid, There is no such national code"),
        )
