#Observer

from config import Config
from notifier import SlackNotifier, Observer
from item import Item

class Inventory:
    ...
    def notify(self, message):
        config = Config()
        if not config.notifications_enabled:
            return
        for observer in self.observers:
            observer.update(message)

    def add_observer(self, observer):
        self.observers.append(observer)

    def __init__(self):
        self.items = []
        self.observers = []
        self.add_observer(SlackNotifier())


    def add_item(self, item):
        self.items.append(item)
        self.notify(f"{item.name}が追加されました")

    def show_all(self):
        for item in self.items:
            print(item)

    def show_discounted_prices(self):
        for item in self.items:
            print(f"{item.name}: {item.get_discounted_price()}円")