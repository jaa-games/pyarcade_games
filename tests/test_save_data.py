from pyarcade_games.save_data import save_data, retrive_value





def test_save_data():
    # Arrange
    save_data("dummy_variable", 5)
    expected = 5
    # Actual
    actual = retrive_value("dummy_variable")
    # Assert
    assert actual == expected


def test_save_data_stromg():
    # Arrange
    save_data("dummy_string_variable", "I am a lovely string")
    expected = "I am a lovely string"
    # Actual
    actual = retrive_value("dummy_string_variable")
    print(actual)
    # Assert
    assert actual == expected


def test_save_data_retrieve_non():
    # Arrange
    expected = None
    # Actual
    actual = retrive_value("non_existant_value")
    # Assert
    assert actual == expected




if __name__=="__main__":
    test_save_data_stromg()