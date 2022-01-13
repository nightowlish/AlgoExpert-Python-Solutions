def taskAssignment(k, tasks):
    nr_tasks = 2 * k
    sorted_task_mapping = sorted({index: t for index, t in enumerate(tasks)}.items(), key=lambda x: x[1])
    
    worker_map = []
    for index in range(k):
        worker_map.append([sorted_task_mapping[index][0], sorted_task_mapping[nr_tasks - index - 1][0]])
    return worker_map
