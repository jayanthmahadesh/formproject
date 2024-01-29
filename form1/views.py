

import json

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
# from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import RadioSelection, Rating, User, tab_one_model


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(email=email, password=password)
        user.save()

        return redirect('tab1')  # Redirect to a success page

    return render(request, 'register.html')


def tab1(request):
    return render(request, 'tab1.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "User doesn't exist")
            return redirect('login')

        if user.password == password:

            # Save email and cookie in the context
            request.session['email'] = email
            request.session['id'] = user.id

            return redirect('tab1')
        else:
            messages.error(request, "Incorrect password")
            return redirect('login')

    return render(request, 'login.html')


def tab_one(request):
    # For POST requests, handle form submission
    if request.method == 'POST':
        digit = request.POST.get('digit')
        name = request.POST.get('name')
        country = request.POST.get('country')
        city = request.POST.get('city')
        # rating = request.POST.get('rating')
        # Validation
        if not digit or not name:
            return HttpResponse("Invalid input", status=400)

        try:
            digit = int(digit)
        except ValueError:
            return HttpResponse("Invalid digit", status=400)

        # Create and save the new TabOne instance
        # Replace 'TabOne' with your actual model class
        tab_one_instance = tab_one_model(
            digit=digit, name=name, country=country, city=city)
        tab_one_instance.save()

        # Redirect after saving
        return redirect('thanks')

    # For GET requests, render the form
    else:
        # Use request.session instead of session
        user_id = request.session.get('id')
        # Use request.session instead of session
        user_email = request.session.get('email')

        context = dict()
        context['user_id'] = user_id
        context['user_email'] = user_email

        # print(user_id)
        # print(user_email)
        return render(request, 'tab1.html', context)


def thanks(request):
    return render(request, 'thanks.html')


@require_POST
def save_rating(request):
    try:
        data = json.loads(request.body)
        rating_value = data.get('rating')

        if rating_value is not None and 0 <= rating_value <= 5:
            # Create a new Rating instance
            rating = Rating(ratings=rating_value)
            rating.full_clean()  # Validate the model instance
            rating.save()
            return JsonResponse({'status': 'success', 'rating': rating_value})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid rating'})

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})

    except ValidationError as e:
        # Catch any validation errors from the model
        return JsonResponse({'status': 'error', 'message': str(e)})

    except Exception as e:
        # Catch any other unexpected errors
        return JsonResponse({'status': 'error', 'message': 'An unexpected error occurred'})


@require_POST
def save_radio_selection(request):
    selected_color = request.POST.get('color')
    if selected_color in dict(RadioSelection.COLOR_CHOICES).keys():
        RadioSelection.objects.create(color=selected_color)
        return redirect('thanks')  # Redirect to a thank you page
    else:
        return render(request, 'tab1.html', {'error': 'Invalid selection'})
