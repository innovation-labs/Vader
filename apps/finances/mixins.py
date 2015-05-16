import stripe
from django.conf import settings
from apps.common.models import BaseModel


class Stripe(BaseModel):
    """
    class to instantiate stripe and provide methods for charging and handling
    """

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(Stripe, self).__init__(*args, **kwargs)
        stripe.api_key = settings.STRIPE_KEY
        self._stripe = stripe
        # params is a dictionary used to set parameters during a charge life
        # cycle, mostly used in post_save and pre_save methods
        self._params = dict()

    def pre_charge(self, *args, **kwargs):
        """
        to perform before preparing a charge,
        used to set self._params parameter
        """
        pass

    def charge(self, amount_in_cents, description, currency=None, *args, **kwargs):
        self.pre_charge(*args, **kwargs)
        if not currency:
            currency = 'CAD'
        try:
            self._params = self._stripe.Charge.create(
                amount=amount_in_cents,
                currency=currency,
                description=description,
                **self._params
            )
            self.post_charge(*args, **kwargs)
            return True, self._params
        except (self._stripe.error.CardError, self._stripe.error.AuthenticationError) as ce:
            self._params = ce
            return False, self._params

    def post_charge(self, *args, **kwargs):
        """
        to perform after the charge, normally used to set the invoice as paid,
        or things like that.
        """
        pass
