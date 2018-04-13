import glob
import fileinput
import re
root_dir = 'D:/PD/base/Artifacts/'

# All functions take a line as an input and perform specific string
# manipulation operations on it in place and then return the line.

# Oracle does a case sensitive comparison for GUIDS
def updateGuids(line):
    """Updates GUID values to upper case letters for hex characters"""
    pattern = re.compile(r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})')
    matches = pattern.findall(line)
    for oldGuid in matches:
        newGuid = oldGuid.upper()
        line = line.replace(oldGuid, newGuid)
    return line

def updateTimestampDataType(line):
    """Updates the datetime data type to date"""
    insensitive_datetime = re.compile(re.escape('datetime'), re.IGNORECASE)
    return insensitive_datetime.sub("date", line)

def getHoursMilitaryTime(hours, isPM):
    if isPM:
        adjusted_hours = int(hours) % 12
        return str(adjusted_hours + 12)
    elif not isPM and hours == '12':
        return '00'
    return str(hours)

def updateTimestampData(line):
    """Changes timestamps from sql to oracle format. 1/1/1900 12:00:00 AM => 1900-1-1 00:00:00 9/25/2017 7:20:50 PM => 2017-9-25 19:20:50"""
    date_pattern = re.compile(r'((\d+)/(\d+)/(\d+) (\d+):(\d+):(\d+) (\w\w))')
    matches = re.findall(date_pattern, line)
    for match in matches:
        month = match[1]
        day = match[2]
        year = match[3]
        isPM = match[7] == 'PM'
        hours = getHoursMilitaryTime(match[4], isPM)
        minutes = match[5]
        seconds = match[6]

        # Create the oracle friendly string
        replacement_text = '{0}-{1}-{2} {3}:{4}:{5}'.format(
            year, month, day, hours, minutes, seconds)

        originalDateTime = match[0]
        line = line.replace(originalDateTime, replacement_text)
    return line

if __name__ == "__main__":
    for filename in glob.iglob(f'{root_dir}**/*.sql', recursive=True):
        for line in fileinput.input(filename, inplace=True):
            try:
                line = updateGuids(line) #T5492
                line = updateTimestampData(line) #T6067
            except Exception as e:
                print(e)
            print(line, end='')
    #for filename in glob.iglob(f'{root_dir}**/*.ddl', recursive=True):
    #    for line in fileinput.input(filename, inplace=True):
    #        try:
    #            line = updateTimestampDataType(line) #T5492
    #        except Exception as e:
    #            print(e)
    #        print(line, end='')