# Python-JSON-SaveData
This python module helps you easily create save data for your python app or game! It only requires a few function calls to work, and uses default python modules, so no need to install any other modules. There is no need to credit me but it would be appreciated.

## QuickStart Guide
1. To start you must download ``save_data.py`` from link[ here](https://github.com/BlurrySquire/Python-JSON-SaveData/blob/main/save_data.py).
2. Paste this code into the start of your main python file:
```python
import save_data as save # import the module

# create the dictionary containing the default save file
default_save = {
  "value": "value"
}

# set the default save file
save.set_default_save(default_save)

# create the save file
save.create('save', default_save, indent=4)

# read the save file to a variable
sd = save.read_save()

# edit the values in the save file
sd["value"] = 'edited_value'

# write the save file
save.write_save(sd, indent=4)
```
3. Mess around with the default_save dictionary, in your code, for your save file.
4. You now have a working save file!

## Notices
- There is more documentation coming soon, that will explain how to use each function.
- The code isnt perfect, if there is any errors please let me know on discord.
- My discord is: ``BlurrySquire#4961``.
