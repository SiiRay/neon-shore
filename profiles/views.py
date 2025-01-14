from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm



def profile(request):
    """ Display the user's overall profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)

def profile_details(request):
    """ Display the user's profile details. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')

    form = UserProfileForm(instance=profile)

    template = 'profiles/details.html'
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, template, context)

def profile_orders(request):
    """ Display the user's orders. """
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/orders.html'
    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

def profile_account(request):
    """ Display the user's account information. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/account.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
