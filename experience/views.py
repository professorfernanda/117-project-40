from django.shortcuts import render
from .models import Experience

# Create your views here.
def experience_list(request):
    experiences = Experience.objects.all()

    return render(request, 'experience/list.html', {
        'experiences': experiences
    })