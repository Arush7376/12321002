# Submission Notes

## What I Implemented

I split the work into three parts:

1. Shared request logging middleware.
2. Vehicle maintenance scheduling.
3. Notification priority inbox.

The vehicle scheduler and notification inbox both call the evaluation APIs and store the responses in separate folders so the output can be checked without calling the API again.

## Algorithm Choices

For vehicle scheduling, I used 0/1 knapsack dynamic programming because each task can either be selected or skipped. The mechanic-hour budget is the capacity, task duration is the cost, and impact is the value.

For the priority inbox, I used a priority rule where placement notifications come before results, and results come before events. Within the same type, newer notifications come first. For a stream of incoming notifications, a min-heap of size 10 is enough to keep the current top notifications.

## Files To Check

- `logging_middleware/middleware.py`
- `vehicle_maintenance_scheduler/src/services/maintenance_scheduler.py`
- `vehicle_maintenance_scheduler/vehicle_scheduling/schedule_solution.json`
- `notification_app_be/src/services/priority_inbox.py`
- `notification_app_be/priority_inbox/top_10_notifications.json`

## Current Limitations

- The evaluation APIs are external, so results can change when the APIs return a new dataset.
- The Django apps include extra folders for normal backend layers, but the main evaluation logic is kept in service classes.
- Database models are not added for the evaluation data because the instructions say not to store the fetched API data in a database.
