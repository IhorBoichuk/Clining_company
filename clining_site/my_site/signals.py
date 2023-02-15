# from paypal.standard.ipn.signals import valid_ipn_received
# from paypal.standard.models import ST_PP_COMPLETED
# from django.shortcuts import redirect
# from django.dispatch import receiver
# from clining_site import settings
# from .models import Contact








# def post_save_contact(sender, **kwargs):
#     print("Request finished!")

# @receiver(valid_ipn_received)
# def contact_received(sender, **kwargs):
#     ipn_obj = sender
#     if ipn_obj.payment_status == 'Completed':
#         o = Order()
#         o.receipt=ipn_obj.invoice
#         o.date_create=ipn_obj.payment_date
#         # WARNING !
#         # Check that the receiver email is the same we previously
#         # set on the `business` field. (The user could tamper with
#         # that fields on the payment form before it goes to PayPal)
#         if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
#             print('Not a valid payment')
#             return 
#         # ALSO: for the same reason, you need to check the amount
#         # received, `custom` etc. are all what you expect or what
#         # is allowed.

#         # Undertake some action depending upon `ipn_obj`.
#         if ipn_obj.payment_gross >= float(settings.PAYPAL_AMOUNT) and ipn_obj.mc_currency == 'USD' :
#             o.save()
#             return 
        
#         print("Invalid amount received!") 
#         return 
#     else:
#         print('Payment not conpleted')
#         return 