import blueprint.app


def test_app(capsys, caplog, example_fixture):
    first_name = example_fixture
    blueprint.app.app(first_name)
    assert "Hello Alex" in caplog.text
