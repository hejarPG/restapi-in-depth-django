from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', view=views.snippet_list),
    path('snippets/<int:pk>/', view=views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)