from django.test import SimpleTestCase

from services.priority_inbox import PriorityInboxService


class PriorityInboxServiceTests(SimpleTestCase):
    def test_prioritizes_type_before_recency(self):
        notifications = [
            {
                "ID": "event-new",
                "Type": "Event",
                "Message": "Newest event",
                "Timestamp": "2026-05-14 10:00:00",
            },
            {
                "ID": "placement-old",
                "Type": "Placement",
                "Message": "Older placement",
                "Timestamp": "2026-05-13 10:00:00",
            },
            {
                "ID": "result-mid",
                "Type": "Result",
                "Message": "Result update",
                "Timestamp": "2026-05-14 09:00:00",
            },
        ]

        result = PriorityInboxService(limit=3).get_top_notifications(notifications)

        self.assertEqual([item["ID"] for item in result], ["placement-old", "result-mid", "event-new"])

    def test_orders_newer_items_first_within_same_type(self):
        notifications = [
            {
                "ID": "placement-old",
                "Type": "Placement",
                "Message": "Older placement",
                "Timestamp": "2026-05-13 10:00:00",
            },
            {
                "ID": "placement-new",
                "Type": "Placement",
                "Message": "Newer placement",
                "Timestamp": "2026-05-14 10:00:00",
            },
        ]

        result = PriorityInboxService(limit=2).get_top_notifications(notifications)

        self.assertEqual([item["ID"] for item in result], ["placement-new", "placement-old"])
