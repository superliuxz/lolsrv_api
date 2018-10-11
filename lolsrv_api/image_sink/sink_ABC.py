from abc import ABC, abstractmethod


class SinkABC(ABC):

    @abstractmethod
    def save(self, commit_repo: str, commit_date: str, commit_sha: str, commit_img):
        """save an individual lol commit
        commit_img is an InMemoryUploadedFile
        """
        pass

    @abstractmethod
    def retrieve_all(self) -> list:
        """returns a list of all sync'ed sha
        """
        pass
