from task_tracker.core import add_task, list_tasks, save_tasks, remove_task, mark_as_concluded

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


def test_remove_task():
    save_tasks([])

    add_task('A')
    add_task('B')
    add_task('C')

    result = remove_task(3)

    assert result is True
    assert len(list_tasks()) == 2
    assert all(task['id'] != 3 for task in list_tasks())


def test_mark_as_concluded_success():
    save_tasks([])

    add_task('ABC')
    add_task('XYZ')

    task_concluded = mark_as_concluded(2)

    assert task_concluded == 'done'

    tasks = list_tasks()
    assert tasks[1]['done'] is True


def test_mark_as_concluded_alredy_done():
    save_tasks([])

    add_task('ABC')
    mark_as_concluded(1)

    result = mark_as_concluded(1)

    assert result == 'already done'


def test_mark_as_concluded_not_found():
    save_tasks([])

    add_task('FGH')

    task_not_found = mark_as_concluded(999)

    assert task_not_found == 'not found'