from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class InstagramVIP(Subject):
    def __init__(self):
        super().__init__()
        self.observers_collection = []
    
    def register_observer(self, observer: Observer):
        self.observers_collection.append(observer)
    
    def remove_observer(self, observer: Observer):
        self.observers_collection.pop()

    def notify_observer(self):
        for observer in self.observers_collection:
            observer.update()
    
    def new_post(self):
        print('Created new post...')
        self.notify_observer()


class Follower(Observer):
    def __init__(self, username: str) -> None:
        self.username = username

    def update(self):
        print(f'{self.username} has been notified!')
    

if __name__ == '__main__':
    follower1 = Follower('John')
    follower2 = Follower('Mary')
    vip = InstagramVIP()
    vip.register_observer(follower1)
    vip.register_observer(follower2)
    vip.new_post()
    vip.remove_observer(follower1)
    vip.new_post()