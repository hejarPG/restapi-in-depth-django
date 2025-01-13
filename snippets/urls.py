from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', view=views.SnippetList.as_view()),
    path('snippets/<int:pk>/', view=views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)