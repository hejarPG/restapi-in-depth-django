from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics, status

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet
    serializer_class = SnippetSerializer