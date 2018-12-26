"""
Implementing an iterator by implementing both __iter__ and __next__ in the same class.
Not a recommended way to iterators. For one, this doesn't support multiple active
scans.

URL: http://www.pythontraininghq.com
Author: Waqas Younas <waqas@pythontraininghq.com>
"""


class Emails:
    def __init__(self, emails):
        self.emails = emails
        self.index = 0

    def __iter__(self):
        return self

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

print("Iterating again")

for email in emails:
    print(email)