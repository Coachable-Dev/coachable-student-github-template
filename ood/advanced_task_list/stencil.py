class Task:
    '''
    Represents a task with a description, due date, and completion status.

    - The task description should be a non-empty string.
    - The due date should be a string in the format 'YYYY-MM-DD'.
    - Completion status should default to False.

    Edge Cases:
    - Raise a ValueError if the description is empty.
    - Raise a ValueError if the due date is not in the correct format.
    '''
    def __init__(self, description: str, due_date: str) -> None:
        # Initialize instance variables for task description, due date, and completion status
        pass

class TodoList:
    '''
    Represents a to-do list containing multiple tasks.

    - The list should be initialized empty.
    '''
    def __init__(self) -> None:
        # Initialize a list to hold tasks
        pass

    '''
    Adds a task to the to-do list.

    Edge Cases:
    - Ensure the task is an instance of the Task class.
    - Raise a ValueError if the task is already in the list.
    '''
    def add_task(self, task: Task) -> None:
        # Method to add a task to the list
        pass

    '''
    Removes a task from the to-do list.

    Edge Cases:
    - Raise a ValueError if the task is not in the list.
    '''
    def remove_task(self, task: Task) -> None:
        # Method to remove a task from the list
        pass

    '''
    Marks a task as completed.

    Edge Cases:
    - Raise a ValueError if the task is not in the list.
    - Raise a ValueError if the task is already completed.
    '''
    def complete_task(self, task: Task) -> None:
        # Method to mark a task as completed
        pass

    '''
    Returns a list of all incomplete tasks.

    - The list should include tasks that have not been marked as completed.
    '''
    def incomplete_tasks(self) -> list[Task]:
        # Return a list of all incomplete tasks
        pass

    '''
    Returns a list of tasks due by a specific date.

    - The list should include tasks with a due date on or before the specified date.
    - Ensure the date format is 'YYYY-MM-DD'.

    Edge Cases:
    - Raise a ValueError if the date is not in the correct format.
    '''
    def tasks_due_by(self, date: str) -> list[Task]:
        # Return a list of tasks due by the specified date
        pass

    '''
    Prioritizes a task by moving it to the top of the list.

    - The prioritized task should appear first in the list of tasks.

    Edge Cases:
    - Raise a ValueError if the task is not in the list.
    '''
    def prioritize_task(self, task: Task) -> None:
        # Method to prioritize a task by moving it to the top of the list
        pass

    '''
    Sorts all tasks by their due date.

    - Tasks should be ordered from earliest to latest due date.

    Edge Cases:
    - Handle cases where tasks have the same due date.
    '''
    def sort_tasks_by_due_date(self) -> None:
        # Method to sort all tasks by their due date
        pass