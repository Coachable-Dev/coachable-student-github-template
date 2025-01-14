def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    #count frequency of each task
    task_counts = Counter(tasks)

    #Find the task with maximum frequency
    max_freq = max(task_counts.values())

    #Count how many tasks have the maximum frequency
    max_freq_tasks = sum(1 for count in task_counts.values() if count == max_freq)

    #Calculate minimum intervals required
    #1. (max_freq - 1) * (n + 1) represents the minimum slots
    #needed for all but the last occurrence of the most frequent
    #task, including cooling periods.
    #2. max_freq_tasks represents the slots needed for tasks with
    #max frequency that need to be placed at the end.
    min_intervals = (max_freq - 1) * (n + 1) + max_freq_tasks

    # Return the maximum of calculated minimum intervals and total
    #tasks.
    #This handles cases where we have enough different tasks to
    #fill cooling periods.
    return max(min_intervals, len(tasks))

    #time O(n)
    #space O(1)
