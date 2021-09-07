from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from datetime import date
# here in this python file we are creating a validator methods that can be called from any model/form.
# it will help avoid code replication

def validate_name(): 
    name_validator = RegexValidator(r'^[a-zA-Z]+$','Names contain non alphabetic character(s), only alphabets are allowed')
    return name_validator

def validate_ctzn_reg_no():
    ctzn_reg_no_validator = RegexValidator(r'(^[A-Z]{2}[0-9]{10}$)', 'Invalid citzen registration number')
    return ctzn_reg_no_validator

def validate_voter_reg_no():
    voter_reg_no_validator = RegexValidator(r'', 'Invalid voter registration number')
       
def validate_age(value):

    today = date.today()
    return today.year - value.year

    if value < 18:
        raise ValidationError("Less than 18 Years old, You are not allowed to register as a voter")
    elif value > 125:
        raise ValidationError("Provided age is not valid")
    else:
        return value



         
