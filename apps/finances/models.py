from django.db import models

from django_pgjson.fields import JsonField

from apps.common.models import *
from .mixins import Stripe

# Create your models here.

class BasePaymentModel(Stripe, TimeStamped):
    """Basic Payment Model, inherits Stripe model, will be used for multiple


    Attributes:
        amount (Decimal): total amount charged to customer
        attempted_on (Time): time on which the charge was attempted
        attempts (Int): Number of times we tried to charge
        charged_on (Time): If charge was succesful, populate the field with current time
        gateway_response (Json): Response from the server
        is_paid (Bool): if charge was succesful
        service_charges (Decimal): Service charges if any, amount is inclusive of service_charges
        taxes (Decimal): Taxes if any, Note: amount is inclusive of taxes
    """
    amount = models.DecimalField(default=0.00, max_digits=20, decimal_places=4)
    attempts = models.IntegerField(default=0)

    #service charges
    service_charges = models.DecimalField(default=0.00, max_digits=20, decimal_places=4)
    taxes = models.DecimalField(default=0.0, max_digits=20, decimal_places=4)
    #total_amount = models.DecimalField(default=0.00, max_digits=20, decimal_places=4)

    # extra timestamps
    attempted_on = models.DateTimeField(blank=True, null=True)
    charged_on = models.DateTimeField(blank=True, null=True)

    gateway_response = JsonField(default={})
    is_paid = models.BooleanField(default=False)

    class Meta:
        abstract = True

    @property
    def line_items_total(self):
        return self.amount - self.service_charges - self.taxes



class Invoice(BasePaymentModel):
    company = models.ForeignKey('companies.Company', related_name='invoices')


class Plan(TimeStamped):
    [UNTIL_EXPIRY, MONTHLY, QUARTERLY, YEARLY] = range(4)
    DURATION_CHOICES = [
        (MONTHLY, 'Monthly'),
        (QUARTERLY, 'Quarterly'),
        (YEARLY, 'Yearly'),
        (UNTIL_EXPIRY, 'Expires on Consumption')
    ]
    amount = models.DecimalField(default=0.00, max_digits=20, decimal_places=4)
    name = models.CharField(max_length=128)
    matric_name = models.CharField(max_length=128)
    duration = models.IntegerField(choices=DURATION_CHOICES, default=UNTIL_EXPIRY)

    def __unicode__(self):
        if self.duration == self.UNTIL_EXPIRY:
            return '%d %s' %(self.amount, self.matric_name)
        else:
            return '%d %s %s' %(self.amount, self.matric_name, self.duration)
