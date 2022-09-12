from main import get_filename


def test_default_case():
    filename = "almaty.jpg"
    result = get_filename(filename)

    assert result == "almaty"