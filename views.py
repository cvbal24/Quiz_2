from django.shortcuts import render, redirect # Import redirect
from django.http import Http404 # Import Http404 for proper error handling
from django.views.decorators.http import require_POST # Import require_POST decorator

sample_users = [
    {'id': 1, 'first_name': 'Blossom', 'last_name': 'Wilson', 'email': 'blossom.wilson@email.com'},
    {'id': 2, 'first_name': 'Bubbles', 'last_name': 'Doe', 'email': 'bubbles.doe@example.com'},
    {'id': 3, 'first_name': 'Buttercup', 'last_name': 'Smith', 'email': 'buttercup.smith@example.com'},
]

def user_list(request):
    """
    Renders the list of users (applicants).
    """
    context = {
        'users': sample_users
    }
    return render(request, 'index.html', context)

def user_detail(request, user_id):
    """
    Renders the detail page (applicant's proposal) for a specific user.
    """
    user = None

    for u in sample_users:
        if u['id'] == user_id:
            user = u
            break


    if user is None:
        raise Http404("Applicant does not exist")

    context = {
        'user': user
    }
    return render(request, 'detail.html', context)

@require_POST
def delete_user(request, user_id):
    """
    Deletes a user (applicant) from the sample_users list and redirects to the user list.
    In a real application, this would interact with a database to delete the User
    and their associated Proposal Object.
    """
    global sample_users
    initial_len = len(sample_users)
    sample_users = [u for u in sample_users if u['id'] != user_id]

    if len(sample_users) == initial_len:

        raise Http404("Applicant does not exist or could not be deleted.")

    return redirect('user_list') # Redirect back to the applicant list page
