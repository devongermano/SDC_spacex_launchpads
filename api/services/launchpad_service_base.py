from abc import ABC, abstractmethod


"""A python abstract base class that we inherit our services from."""
class LaunchpadServiceBase(ABC):

    @abstractmethod
    def get_launchpads(self):
        pass

    @abstractmethod
    def get_launchpad_by_id(self, padid: int):
        pass
