import logging
import swapper
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

logger = logging.getLogger(__name__)


@receiver(user_signed_up)
def create_customer_on_signup(sender, user, request, **kwargs):
    customer_model = swapper.load_model('flexible_plans', 'Customer')
    customer, created = customer_model.objects.get_or_create(user=user)
    if created:
        logger.info("New Customer created for user %s" % user)
    else:
        logger.warning("Customer already created %s" % customer)


