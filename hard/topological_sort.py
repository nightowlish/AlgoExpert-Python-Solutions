def getJobsWithoutDeps(job_map, visited):
    return {job for job in job_map if not job_map[job] - visited}
    
def removeDependencies(job_map, jobs):
    for job in jobs:
        del job_map[job]

def getOrder(jobs, job_map, visited):
    order = []
    while job_map:
        jobs_without_deps = getJobsWithoutDeps(job_map, visited)
        if not jobs_without_deps:
            return []
        order.extend(jobs_without_deps)
        visited.update(jobs_without_deps)
        removeDependencies(job_map, jobs_without_deps)
    return order
        
def topologicalSort(jobs, deps):
    job_map = {job: set() for job in jobs}
    for dep in deps:
        job_map[dep[1]].add(dep[0])
    return getOrder(jobs, job_map, set())
