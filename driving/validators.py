from django.core.validators import RegexValidator


def _validator():

    first_part = r'/d{2}'
    alphabet_part = r'(الف|ب|پ|ت|ج|د|س|ص|ط|ق|ک|ع|ل|م|ن|و|ه|ی)+'  # (simple regex, validated ))
    second_part = r'/d{3}'
    city_code = r'/d{2}'

    regex = (first_part+alphabet_part+second_part,city_code)
    return RegexValidator(regex,message='Enter a valid Domain (Not a URL)',code='invalid_domain')


number_plate_validator = _validator()