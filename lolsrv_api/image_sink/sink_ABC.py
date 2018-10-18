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

    @classmethod
    def __subclasshook__(cls, C):
        """
        https://docs.python.org/3/library/abc.html#abc.ABCMeta.__subclasshook__

        The __subclasshook__() class method defined here says that any class
        that has an save() and retrieve_all() methods in its __dict__ (or in
        that of one of its base classes, accessed via the __mro__ list) is
        considered a SinkABC too.
        """
        if cls is SinkABC:
            if any("save" in B.__dict__ for B in C.__mro__) and \
                    any("retrieve_all" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
