from background_task import background


@background(schedule=5)
def test_task():
    """
    Test background task
    :return:
    """
    print('Test background task')

