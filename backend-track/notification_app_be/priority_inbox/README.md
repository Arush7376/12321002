# Priority Inbox Output

This folder stores Stage 6 notification priority-inbox artifacts.

- `notifications_response.json`: raw response fetched from the evaluation Notification API.
- `top_10_notifications.json`: computed top 10 unread notifications.

Ranking rule:

1. `Placement`
2. `Result`
3. `Event`

For notifications with the same type, the newest timestamp appears first.
