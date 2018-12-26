"""
Iterator implemented by using generators (recommended way to add iteration support in Python).
URL: http://www.pythontraininghq.com
Author: Waqas Younas <waqas@pythontraininghq.com>
"""
class Emails:
    def __init__(self, emails):
        self.emails = emails

    def __iter__(self):
        for email in self.emails:
            yield email


emails = Emails(['a@example.org', 'b@example.org', 'c@example.org'])
for email in emails:
    print(email)

print("Iterating again")

for email in emails:
    print(email)