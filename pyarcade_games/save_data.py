"""
Saving Data To Local Module
"""
import os

def save_data(variable_name: str, value):
    """Save data to a local storage.

    Args:
        variable_name (str): [name of the variable to be saved.]
        value ([type]): [value type]
    Returns;
        None
    """
    if not os.path.exists("games_data"):
        os.makedirs("games_data")
        init_path = "games_data/__init__.py"
        with open(init_path, "a+") as init:
            init.write(f"__version__ = '0.1.0'")

    file_path = "games_data/saves.py"
    with open(file_path, "a+") as saves_data:
        if type(value) == str:
            saves_data.write(f"{variable_name} = '{value}'\n")
        else:
            saves_data.write(f"{variable_name} = {value}\n")


def retrive_value(variable_name):
    value = None
    try:
        import games_data.saves as saves
        value = getattr(saves, variable_name)
    except:
        pass
    return value



if __name__ == "__main__":
    save_data("test_data",5)
    save_data("maximum_lvl","i am a string")
    save_data("gravity_range",99)