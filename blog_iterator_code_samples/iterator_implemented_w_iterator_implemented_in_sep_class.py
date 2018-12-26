"""
Iterator implemented by using a separate Iterator class. This one is also not idiomatic Python.
URL: http://www.pythontraininghq.com
Author: Waqas Younas <waqas@pythontraininghq.com>
"""


class Emails:
    def __init__(self, emails):
        self.emails = emails

    def __iter__(self):
        return EmailIterator(self.emails)


class EmailIterator:

    def __init__(self, emails):
        self.emails = emails
        self.index = 0

    def __next__(self):
        try:
            email = self.emails[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return email


emails = Emails(['a@example.org', 'b@example.org', 'c@example.org'])
for email in emails:
    print(email)

print("Iterate again")

for email in emails:
    print(email)