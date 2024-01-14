from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST


@require_GET
def num_to_english_get(request):
    return JsonResponse({'status': 'error', 'message': 'Not Implemented'})


@require_POST
def num_to_english_post(request):
    return JsonResponse({'status': 'error', 'message': 'Not Implemented'})
