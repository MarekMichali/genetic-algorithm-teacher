from abc import abstractmethod


class ExampleInterface:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def show_info(self, title, message, selection_callback, best_sols):
        pass

    @abstractmethod
    def on_selection(self, sender, unused, user_data):
        pass

    @abstractmethod
    def error(self, title, selection_callback):
        pass
