from django.dispatch import Signal

"""
Signals to emit to coordinate with other applications depending on flexible_plans
"""

customer_created = Signal(providing_args=['customer'])
customer_created.__doc__ = """
Sent after the creation of the Customer associated to the User
"""

subscription_activate = Signal(providing_args=['subscription'])
subscription_activate.__doc__ = """
Sent after the activation of the Customer Subscription
"""

subscription_deactivate = Signal(providing_args=['subscription'])
subscription_deactivate.__doc__ = """
Sent after the deactivation of the Customer Subscription
"""

subscription_cancel = Signal(providing_args=['subscription'])
subscription_cancel.__doc__ = """
Sent after the Customer cancels the Subscription
"""


subscription_end = Signal(providing_args=['subscription'])
subscription_end.__doc__ = """
Sent after the Subscription ends
"""

