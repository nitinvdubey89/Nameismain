#A task is a reusable piece of code that implements some
# functionality for a single host.
# In python terms it is a function that takes a Task as first paramater and returns a Result.


from nornir.core.task import Task, Result

def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world!"
    )