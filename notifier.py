#Observer

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class EmailNotifier(Observer):
    def update(self, message):
        print(f"メール通知: {message}")

class SlackNotifier(Observer):
    def update(self, message):
        print(f"Slack通知: {message}")