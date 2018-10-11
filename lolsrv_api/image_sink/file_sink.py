import glob
import os

from lolsrv_api.image_sink.sink_ABC import SinkABC


class FileSink(SinkABC):
    def __init__(self, path):
        self.path = path

    def save(self, commit_repo: str, commit_date: str, commit_sha: str, commit_img):
        p = self.path+'/'+commit_repo
        if not os.path.isdir(p):
            os.makedirs(p)
        filename = f'{commit_date}_{commit_sha}.jpg'
        with open(p+'/'+filename, 'wb+') as dest:
            for chunk in commit_img.chunks():
                dest.write(chunk)

    def retrieve_all(self) -> list:
        shas = []
        for filename in glob.iglob(self.path+'/**/*.jpg', recursive=True):
            sha = filename.split('_')[-1].split('.')[0]
            shas.append(sha)
        return shas
