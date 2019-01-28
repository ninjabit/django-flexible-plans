from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


def subscription_status(request):
    """
    User Subscription Context Processor, to keep the Subscription Status available in the templates
     * ``ACCOUNT_EXPIRED = boolean``, account was expired state,
     * ``ACCOUNT_NOT_ACTIVE = boolean``, set when account is not expired, but it is over quotas so it is
                                        not active
     * ``EXPIRE_IN_DAYS = integer``, number of days to account expiration,
     * ``EXTEND_URL = string``, URL to account extend page.
     * ``ACTIVATE_URL = string``, URL to account activation needed if  account is not active

    :param request: HttpRequest object
    :return: the current user susbscription status object
    """
    if request.user.is_authenticated:
        try:
            return {
                'ACCOUNT_EXPIRED': request.user.subscription.is_expired(),
                'ACCOUNT_NOT_ACTIVE': (
                not request.user.subscription.is_active() and not request.user.subscription.is_expired()),
                'EXPIRE_IN_DAYS': request.user.subscription.days_left(),
                'EXTEND_URL': reverse('current_plan'),
                'ACTIVATE_URL': reverse('account_activation'),
            }
        except ObjectDoesNotExist:
            pass
    return {}