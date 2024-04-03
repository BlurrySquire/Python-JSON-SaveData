from save_data import *

if __name__ == "__main__":
    save_file_data = {
        "user_info": {
            "username": "guest user"
        },
        "wins": 0,
        "loses": 0
    }

    save_file = SaveFile("test.json")

    save_file.write(save_file_data)
    print(save_file.read())

    save_file_data["wins"] = 1
    save_file.write(save_file_data)
    print(save_file.read())
