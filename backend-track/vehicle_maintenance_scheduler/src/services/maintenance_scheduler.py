from dataclasses import dataclass


@dataclass(frozen=True)
class MaintenanceTask:
    task_id: str
    duration: int
    impact: int


class MaintenanceSchedulerService:
    """Solve the depot maintenance planning problem using 0/1 knapsack DP."""

    def select_tasks(self, tasks: list[MaintenanceTask], mechanic_hours: int) -> dict:
        task_count = len(tasks)
        dp = [[0] * (mechanic_hours + 1) for _ in range(task_count + 1)]

        for index, task in enumerate(tasks, start=1):
            for capacity in range(mechanic_hours + 1):
                dp[index][capacity] = dp[index - 1][capacity]
                if task.duration <= capacity:
                    candidate = dp[index - 1][capacity - task.duration] + task.impact
                    dp[index][capacity] = max(dp[index][capacity], candidate)

        selected_tasks = []
        remaining_capacity = mechanic_hours
        for index in range(task_count, 0, -1):
            if dp[index][remaining_capacity] != dp[index - 1][remaining_capacity]:
                task = tasks[index - 1]
                selected_tasks.append(task)
                remaining_capacity -= task.duration

        selected_tasks.reverse()
        return {
            "mechanicHours": mechanic_hours,
            "totalDuration": sum(task.duration for task in selected_tasks),
            "totalImpact": sum(task.impact for task in selected_tasks),
            "selectedTaskIds": [task.task_id for task in selected_tasks],
            "selectedTasks": [
                {
                    "TaskID": task.task_id,
                    "Duration": task.duration,
                    "Impact": task.impact,
                }
                for task in selected_tasks
            ],
        }
