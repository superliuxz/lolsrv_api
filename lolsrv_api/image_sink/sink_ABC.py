from abc import ABC, abstractmethod


class SinkABC(ABC):

    @abstractmethod
    def sink(self):
        pass

    @abstractmethod
    def sink_all(self):
        pass

    @abstractmethod
    def retrieve(self):
        pass

    @abstractmethod
    def retrieve_all(self):
        pass
