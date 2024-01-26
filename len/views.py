from django.shortcuts import render
from .models import Lens
# Create your views here.
def home(request):
    lens = {
        'lens': Lens.objects.all(),
    }
    return render(request, 'pages/index.html', lens)