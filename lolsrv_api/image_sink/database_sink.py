from django.utils.dateparse import parse_datetime

from lolsrv_api.image_sink.sink_ABC import SinkABC
from lolsrv_api.models import Images


class DatabaseSink(SinkABC):
    def save(self, commit_repo: str, commit_date: str, commit_sha: str, commit_img):
        img = Images(
            repo=commit_repo,
            date=parse_datetime(commit_date),
            sha=commit_sha,
            img=commit_img.read(),
        )
        img.save()

    def retrieve_all(self):
        imgs = Images.objects.all()
        return [img.sha for img in imgs]
