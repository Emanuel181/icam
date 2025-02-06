from django.shortcuts import render

def poll_view(request, poll_id):
    return render(request, '../templates/polls/polls.html', {'poll_id': poll_id})

