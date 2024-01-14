from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from .utils import convert_number_to_english


@require_GET
def num_to_english_get(request):
    return num_to_english_return(request.GET.get('number'))


@require_POST
def num_to_english_post(request):
    return num_to_english_return(request.POST.get('number'))


def num_to_english_return(request_number: str):
    try:
        if not request_number:
            return JsonResponse({'status': 'error', 'message': 'Number must not be null'}, status=400)
        number = float(request_number)
        number_in_english = convert_number_to_english(number)
        return JsonResponse({'status': 'ok', 'num_in_english': number_in_english}, status=200)
    except ValueError:
        return JsonResponse({'status': 'error', 'message': 'Invalid number'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'Unexpected Exception'}, status=500)
