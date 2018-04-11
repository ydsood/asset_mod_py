# asset_mod_py
Python script to modify FAST assets and overlay sql's

### Executing this script
#### First Time
- Install Python 3.6.5

#### Every Time
- Navigate to the directory where the script is located
- Edit the `root_dir` constant to point to the location where you want to execute this script
```python
#Example
root_dir = 'D:/PD/base/Spreadsheets/'
```
- Open terminal window of choice (CMD / Powershell / Bash ) that has python setup and execute this command
```bash
py asset_mod
```

### Adding new methods
Methods should follow this interface for testability.

methodName (<str> line) => <str> modifiedLine

**Example**
  
```python

def updateGuids(line):
    pattern = re.compile(r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})')
    matches = pattern.findall(line)
    for oldGuid in matches:
        newGuid = oldGuid.upper()
        line = line.replace(oldGuid, newGuid)
    return line

```

### Unit tests

The module has been setup for unit testing using the `unittest` module from python. When adding a new method ensure that unit tests are provided for it so the spec is clear for other developers.

**Example**

```python
    def test_UpdateArtifacts_updateGuids(self):
        self.assertEqual( asset_mod.updateGuids('371492ec-7009-43c8-b800-7ba7fe0a2d7e'), '371492EC-7009-43C8-B800-7BA7FE0A2D7E', 'Converts lowercase to uppercase')
        self.assertEqual( asset_mod.updateGuids('371492EC-7009-43C8-B800-7BA7FE0A2D7E'), '371492EC-7009-43C8-B800-7BA7FE0A2D7E', 'does not change upper case')
        self.assertEqual( asset_mod.updateGuids('Test this string'), 'Test this string', 'Does not modify non-guids' )
```
#### Executing unit tests
From the terminal execute this command
```bash
py -m unittest
```
The unittest module discovers tests in the current directory and its children. All methods prefixed with `Test` are executed. The response on the terminal displays a message only when a test throws an error.

## References
- [https://docs.python.org/2/library/unittest.html](Unit Test module from python)
