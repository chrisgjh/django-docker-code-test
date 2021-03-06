from django.db import models
from django.db.models.fields import CharField

MONTHS = (
    ('January', 'JANUARY'),
    ('February', 'FEBRUARY'),
    ('March', 'MARCH'),
    ('April', 'APRIL'),
    ('May', 'MAY'),
    ('June', 'JUNE'),
    ('July', 'JULY'),
    ('August', 'AUGUST'),
    ('September', 'SEPTEMBER'),
    ('October', 'OCTOBER'),
    ('November', 'NOVEMBER'),
    ('December', 'DECEMBER'),
)

DAYOFWEEK = (
    ('Monday', 'MONDAY'),
    ('Tuesday', 'TUESDAY'),
    ('Wednesday', 'WEDNESDAY'),
    ('Thursday', 'THURSDAY'),
    ('Friday', 'FRIDAY'),
    ('Saturday', 'SATURDAY'),
    ('Sunday', 'SUNDAY'),
)

class FavDate(models.Model):
    month = CharField(max_length=20, default='January', choices=MONTHS, null=False)
    dayofweek = CharField(max_length=20, default='Monday', choices=DAYOFWEEK, null=False)