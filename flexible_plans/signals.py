from django.dispatch import Signal

"""
Signals to emit to coordinate with other applications depending on flexible_plans
"""

customer_created = Signal()
customer_created.__doc__ = """
Sent after the creation of the Customer associated to the User
"""

subscription_activate = Signal()
subscription_activate.__doc__ = """
Sent after the activation of the Customer Subscription
"""

subscription_deactivate = Signal()
subscription_deactivate.__doc__ = """
Sent after the deactivation of the Customer Subscription
"""
