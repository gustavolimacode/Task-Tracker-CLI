from task_tracker.core import add_task, list_tasks, save_tasks

def test_add_task():
    save_tasks([])

    task = add_task('First Task')

    assert task['id'] == 1
    assert task['title'] == 'First Task'
    assert task['done'] is False

    tasks = list_tasks()
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'First Task'


def test_list_tasks():
    save_tasks([])

    add_task('First Task')
    add_task('Second Task')

    tasks = list_tasks()

    assert len(tasks) == 2
    assert tasks[0]['title'] == 'First Task'
    assert tasks[1]['title'] == 'Second Task'