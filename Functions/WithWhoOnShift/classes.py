import re, datetime

class Cell:
    def __init__(self, content):
        self.content = content

    def isDate(self):
        return isinstance(self.content, (datetime.datetime, datetime.date))

    def toDate(self):
        return self.content.date()

    def isTime(self):
        time_form = re.compile(r'^\d{2}-\d{2}$')
        return isinstance(self.content, str) and bool(time_form.match(self.content))

    def isTrash(self):
        trash = {'u', 'Name', 'Total Hours', 'shift', 'Max', 'zl', 'Total Paid', 'Shift', 'Hrs', 'Total Month ', 'overtime'}
        return self.content in trash

    def isName(self, name):
        return self.content == name

    def isValid(self, name):
        if isinstance(self.content, str):
            if not self.isTime() and not self.isTrash():
                if not self.isName(name):
                    return True
        return False

    def __repr__(self):
        return str(self.content)

class Day:
    def __init__(self, column):
        pass