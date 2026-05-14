from dataclasses import dataclass
from datetime import datetime
from heapq import heappop, heappush
from typing import Iterable


TYPE_PRIORITY = {
    "placement": 3,
    "result": 2,
    "event": 1,
}


@dataclass(frozen=True)
class Notification:
    id: str
    type: str
    message: str
    timestamp: datetime

    @classmethod
    def from_api_payload(cls, payload: dict) -> "Notification":
        return cls(
            id=payload["ID"],
            type=payload["Type"],
            message=payload["Message"],
            timestamp=datetime.strptime(payload["Timestamp"], "%Y-%m-%d %H:%M:%S"),
        )

    def to_api_payload(self) -> dict:
        return {
            "ID": self.id,
            "Type": self.type,
            "Message": self.message,
            "Timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }


class PriorityInboxService:
    """Find the top unread notifications by category priority and recency.

    Priority order is:
    1. Placement notifications
    2. Result notifications
    3. Event notifications

    Within the same type, newer notifications rank first. For a continuous
    stream, keep a min-heap of size n and evict the lowest ranked item when a
    better notification arrives.
    """

    def __init__(self, limit: int = 10):
        self.limit = limit

    def get_top_notifications(self, notifications: Iterable[dict]) -> list[dict]:
        heap: list[tuple[int, float, str, Notification]] = []

        for payload in notifications:
            notification = Notification.from_api_payload(payload)
            priority_key = self._priority_key(notification)

            if len(heap) < self.limit:
                heappush(heap, (*priority_key, notification.id, notification))
                continue

            if priority_key > heap[0][:2]:
                heappop(heap)
                heappush(heap, (*priority_key, notification.id, notification))

        ranked = sorted(heap, key=lambda item: (item[0], item[1], item[2]), reverse=True)
        return [item[3].to_api_payload() for item in ranked]

    @staticmethod
    def _priority_key(notification: Notification) -> tuple[int, float]:
        type_weight = TYPE_PRIORITY.get(notification.type.lower(), 0)
        recency = notification.timestamp.timestamp()
        return type_weight, recency
