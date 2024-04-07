# Python-JSON-SaveData
This python module helps you easily create save data for your python app or game! It only requires a few function calls to work, and uses default python modules, so no need to install any other modules. There is no need to credit me but it would be appreciated.

![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/BlurrySquire/Python-JSON-SaveData/total?logo=github)
![GitHub Release](https://img.shields.io/github/v/release/BlurrySquire/Python-JSON-SaveData)

## QuickStart Guide
1. To start you must download ``save_data.py`` [here](https://github.com/BlurrySquire/Python-JSON-SaveData/blob/main/save_data.py).
2. This is an example of the usage:
```python
from save_data import *

if __name__ == "__main__":
    # Create a dictionary to contain the save data.
    save_file_data = {
        "user_info": {
            "username": "guest user"
        },
        "wins": 0,
        "loses": 0
    }

    # Create a savefile. If the file doesn't already exist then it creates it.
    save_file = SaveFile("test.json")

    save_file.write(save_file_data)
    print(save_file.read())

    # Modify save data to ensure it is writing the file properly
    save_file_data["wins"] = 1
    save_file.write(save_file_data)
    print(save_file.read())
```
