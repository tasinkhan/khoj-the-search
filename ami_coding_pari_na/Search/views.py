from django.shortcuts import render
from .models import Search
from .serializers import SearchSerializer
from .filters import SearchResultFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from django.contrib.auth.decorators import login_required
# Search Function

@login_required
def search_view(request):
    user_id=request.user.id 
    result = None

    if request.method == 'POST':
        input_values = (request.POST.get('input_values'))
        search_value = int(request.POST.get('search_value'))
        splitted_input_values = input_values.split(',')
        sorted_input_values = []

        for i in splitted_input_values:
            sorted_input_values.append(int(i))
        sorted_input_values.sort(reverse=True)
        search_model = Search.objects.create(input_values=sorted_input_values, user_id=user_id)
        search_model.save()

        if search_value in search_model.input_values:
            result = True
        else:
            result = False

    return render(request,'search/search.html',context={'result':result})

# classBasedView for search result list and API.

class SearchResutListApi(ListAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SearchResultFilter