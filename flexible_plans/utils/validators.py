from django.conf import settings
from django.core.exceptions import ValidationError

from ..helpers.importer import import_name


def plan_validation(user, plan=None, on_activation=False):
    """
    Validates validator that represents quotas in a given system
    :param user:
    :param plan:
    :return:
    """
    if plan is None:
        # if plan is not given, the default is to use current plan of the user
        plan = user.userplan.plan
    quota_dict = plan.get_quota_dict()
    validators = getattr(settings, 'PLANS_VALIDATORS', {})
    validators = import_name(validators)
    errors = {
        'required_to_activate': [],
        'other': [],
    }

    for quota in validators:
        validator = import_name(validators[quota])

        if on_activation:
            validator.on_activation(user, quota_dict)
        else:
            try:
                validator(user, quota_dict)
            except ValidationError as e:
                if validator.required_to_activate:
                    errors['required_to_activate'].extend(e.messages)
                else:
                    errors['other'].extend(e.messages)
    return errors
