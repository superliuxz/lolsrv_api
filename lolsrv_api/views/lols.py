import logging
import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from lolsrv_api.helper import load_class_from_path
from lolsrv_api.settings.lolsrv_api_settings import IMG_SINK_PATH


logger = logging.getLogger("django")

sink = load_class_from_path(IMG_SINK_PATH)()


@method_decorator(csrf_exempt, name="dispatch")
class Uplol(View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        logger.info("hit POST...")

        commit_repo = request.POST.get("repo")
        commit_date = request.POST.get("date")
        commit_sha = request.POST.get("sha")
        commit_img = request.FILES.get("lol")

        sink.save(commit_repo, commit_date, commit_sha, commit_img)

        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name="dispatch")
class Lols(View):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        logger.info("hit GET...")

        shas = sink.retrieve_all()
        return HttpResponse(json.dumps([{"sha": sha} for sha in shas]), status=200)
