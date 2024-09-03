from abc import ABC, abstractmethod


class MessageQueue(ABC):
    @abstractmethod
    def __init__(self, queue_name: str, host: str, port: str, **kwargs) -> None:
        ...

    @abstractmethod
    def enqueue(self, item: bytes) -> None:
        ...

    @abstractmethod
    def message_callback(self, ch, method, properties, body: bytes) -> None:
        ...

    @abstractmethod
    def consumer(self) -> None:
        """阻塞方法"""
        ...
