import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MinimumNumberValidator(object):
    def __init__(self, min_number=2):
        self.min_number = min_number
    
    def validate(self, password, user=None):
        # if len(password) < self.min_number:
        if sum(d.isdigit() for d in password) < 2:
            raise ValidationError(
                _('This password must contain at least %(min_number)d numbers.'),
                code='password_least_two_numbers',
                params={'min_number': self.min_number},
            )

    def get_help_text(self):
        return _(
            'Your password must contain at least %(min_number)d numbers.'
            % {'min_number': self.min_number}
        )


class MinimumSpecialCharacterValidator(object):
    def __init__(self, min_special_character=2):
        self.min_special_character = min_special_character
    
    def validate(self, password, user=None):
        special_char=0
        for i in range(0, len(password)):
            if (password[i].isalpha()):  
                continue
            elif (password[i].isdigit()):
                continue
            else: 
                special_char += 1
        if special_char < 2:
            raise ValidationError(
                _('This password must contain at least %(min_special_character)d special characters.'),
                code='password_least_two_numbers',
                params={'min_special_character': self.min_special_character},
            )

    def get_help_text(self):
        return _(
            'Your password must contain at least %(min_special_character)d special characters.'
            % {'min_special_character': self.min_special_character}
        )


class NoBlankSpaceValidator(object):
    def validate(self, password, user=None):
        for p in password:
            if (p.isspace()) == True:
                raise ValidationError(
                    _('This Password cannot have blank space.'),
                    code='no_blank_space',
                )

    def get_help_text(self):
        return _(
            'Your password must not contain any blank space.'
        )
