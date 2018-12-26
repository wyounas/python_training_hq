"""
Implementing an iterator using __getittem__. This method is not a recommended way to create an
iterator since it exists for backward compatability reasons and maybe deprecated in future.

URL: http://www.pythontraininghq.com
Author: Waqas Younas <waqas@pythontraininghq.com>
"""


class Emails:
    def __init__(self, emails):
        self.emails = emails

    def __getitem__(self, index):
        return self.emails[index]


emails = Emails(['a@example.org', 'b@example.org', 'c@example.org'])
for email in emails:
    print(email)

print("Iterating again")

for email in emails:
    print(email)

a, b, c = emails
print(a, b, c)
print("a@example.org" in emails)