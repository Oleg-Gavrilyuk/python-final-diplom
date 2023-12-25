from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime


# Create your views here.

@api_view(['GET'])
def index(request):
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    data = {
        'URL API ': 'http://127.0.0.1:8000/api/v1/',
        'Django Admin ': 'http://127.0.0.1:8000/admin/login/?next=/admin/',
        'Login': 'admin@gmail.com',
        'Password': 'admin1990'
    }
    return Response(data)
