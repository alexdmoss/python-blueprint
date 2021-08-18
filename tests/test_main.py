import blueprint.main


def test_main(mocker):
    mocker.patch('blueprint.main.app')
    blueprint.main.app()
