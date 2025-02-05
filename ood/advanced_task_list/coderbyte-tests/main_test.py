from stencil import *

def test_task_initialization():
    task = Task("Buy groceries", "2024-12-31")
    assert task.description == "Buy groceries", "Task description should be 'Buy groceries'"
    assert task.due_date == "2024-12-31", "Due date should be '2024-12-31'"
    assert task.completed == False, "Task should not be completed initially"

    # Test edge cases
    try:
        Task("", "2024-12-31")
        assert False, "Task description cannot be empty"
    except ValueError:
        pass

    try:
        Task("Buy groceries", "31-12-2024")
        assert False, "Due date must be in 'YYYY-MM-DD' format"
    except ValueError:
        pass

def test_add_task():
    todo_list = TodoList()
    task = Task("Buy groceries", "2024-12-31")
    todo_list.add_task(task)
    assert task in todo_list.tasks, "Task should be added to the list"

    # Test edge cases
    try:
        todo_list.add_task(task)
        assert False, "Should not allow adding the same task twice"
    except ValueError:
        pass

    try:
        todo_list.add_task("Not a Task object")
        assert False, "Should only add instances of Task"
    except ValueError:
        pass

def test_remove_task():
    todo_list = TodoList()
    task = Task("Buy groceries", "2024-12-31")
    todo_list.add_task(task)
    todo_list.remove_task(task)
    assert task not in todo_list.tasks, "Task should be removed from the list"

    # Test edge cases
    try:
        todo_list.remove_task(task)
        assert False, "Should not allow removing a task that is not in the list"
    except ValueError:
        pass

def test_complete_task():
    todo_list = TodoList()
    task = Task("Buy groceries", "2024-12-31")
    todo_list.add_task(task)
    todo_list.complete_task(task)
    assert task.completed == True, "Task should be marked as completed"

    # Test edge cases
    try:
        todo_list.complete_task(task)
        assert False, "Should not allow completing a task that is already completed"
    except ValueError:
        pass

    try:
        todo_list.complete_task(Task("Walk the dog", "2024-12-31"))
        assert False, "Should not allow completing a task that is not in the list"
    except ValueError:
        pass

def test_incomplete_tasks():
    todo_list = TodoList()
    task1 = Task("Buy groceries", "2024-12-31")
    task2 = Task("Walk the dog", "2024-12-31")
    todo_list.add_task(task1)
    todo_list.add_task(task2)
    todo_list.complete_task(task1)
    incomplete = todo_list.incomplete_tasks()
    assert task1 not in incomplete, "Completed task should not be in incomplete tasks"
    assert task2 in incomplete, "Incomplete task should be in incomplete tasks"

def test_tasks_due_by():
    todo_list = TodoList()
    task1 = Task("Buy groceries", "2024-12-31")
    task2 = Task("Walk the dog", "2024-12-30")
    task3 = Task("Clean house", "2025-01-01")
    todo_list.add_task(task1)
    todo_list.add_task(task2)
    todo_list.add_task(task3)
    
    due_by = todo_list.tasks_due_by("2024-12-31")
    
    assert len(due_by) == 2, "There should be 2 tasks due by 2024-12-31"
    assert task1 in due_by, "Task1 should be due by 2024-12-31"
    assert task2 in due_by, "Task2 should be due by 2024-12-31"
    assert task3 not in due_by, "Task3 should not be due by 2024-12-31"

    # Test edge cases
    try:
        todo_list.tasks_due_by("31-12-2024")
        assert False, "Should raise a ValueError if date is not in 'YYYY-MM-DD' format"
    except ValueError:
        pass