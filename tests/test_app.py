import blueprint.app


# def test_app(capsys, example_fixture):
#     app()
#     captured = capsys.readouterr()

#     assert "Hello World..." in captured.out


# import main


def test_app(capsys, caplog, example_fixture):
    first_name = example_fixture
    blueprint.app.app(first_name)
    assert "Hello Alex" in caplog.text
