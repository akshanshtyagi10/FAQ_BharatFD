from rest_framework.generics import ListAPIView
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
