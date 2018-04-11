import glob
import fileinput
import re
root_dir = 'D:/PD/base/Spreadsheets/'

# All functions take a line as an input and perform specific string
# manipulation operations on it in place and then return the line.

# Oracle does a case sensitive comparison for GUIDS
def updateGuids(line):
    pattern = re.compile(r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})')
    matches = pattern.findall(line)
    for oldGuid in matches:
        newGuid = oldGuid.upper()
        line = line.replace(oldGuid, newGuid)
    return line


if __name__ == "__main__":
    for filename in glob.iglob(f'{root_dir}**/*.sql', recursive=True):
        for line in fileinput.input(filename, inplace=True):
            try:
                line = updateGuids(line) #T5492
            except Exception as e:
                print(e)
            print(line, end='')