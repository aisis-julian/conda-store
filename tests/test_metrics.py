def test_metrics(testclient):
    response = testclient.get('metrics')
    d = {line.split()[0]: line.split()[1] for line in response.content.decode('utf-8').split('\n')}
    assert {'conda_store_disk_free', 'conda_store_disk_total', 'conda_store_disk_usage'} <= d.keys()


def test_celery(testclient):
    response = testclient.get('celery')
    assert response.json().keys() == {
        'active_tasks',
        'availability',
        'registered_tasks',
        'scheduled_tasks',
        'stats',
    }
