from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.



def models_list(request):
        random_n = random.randint(1, 20)
        random_n += random.choice([5, 10, 0])

        if random_n == 1:
            random_n = 2
            message = "Testing of views 2 Bohužel štěstí nepřálo"
        else:
            message = f"Testing of views {random_n}"

        return HttpResponse(message)