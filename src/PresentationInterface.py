from abc import abstractmethod


class PresentationInterface:
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def show_ext(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod 
    def back(self):
        pass
