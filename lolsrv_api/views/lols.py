import logging
import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


logger = logging.getLogger('django')


@method_decorator(csrf_exempt, name='dispatch')
class Uplol(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        logger.info('hit POST...')
        try:
            body = json.loads(request.body.decode('utf-8'))
        except json.decoder.JSONDecodeError:
            logging.info('failed to decode post body')
            return HttpResponseBadRequest()

        return JsonResponse({'body': body}, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class Lols(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        logger.info('hit GET...')
        return JsonResponse({'sha': 123}, status=200)
