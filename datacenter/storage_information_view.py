from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration
from datacenter.models import get_entered_time

def storage_information_view(request):

    visit = Visit.objects.all()[0]
    duration = get_duration(visit)
    entered_at = get_entered_time(visit)

    non_closed_visits = [
        {
            'who_entered': 'Richard Shaw',
            'entered_at': entered_at,
            'duration': duration,
        }
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
