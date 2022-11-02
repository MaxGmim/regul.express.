import re
from pprint import pprint
import csv

with open('phonebook_raw.csv') as f:
    rows = csv.reader(f, delimiter=',')
    contact_list = list(rows)
pprint(contact_list)


phone_list = re.complier(r'(\+7|8)\s*\(?(\d{3})\)?(\s*|-)(\d{3})(\s*|-*)(\d{2})-?(\d{2})(\s*(\(?(\доб.)?)\s*(\d{4}))?(\))*')
text_list = re.complier(r'(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё]\w+[А-яЁё –]*\–*\s*)*\,*(\+*\d\s*\(*\d+\)*\-*\s*\d+\-*\d+\-*\d+\s*\(*\w*\.*\s*\d*\)*)*\,*(\w+\.*\w*\@\w+\.\w+)*')


new_contact_list = []
for i in range(len(contact_list)):
    if i == 0:
        new_contact_list.append(contact_list[i])
    else:
        line = ','.join(contact_list[i])
        result = re.search(text_pattern, line)
        new_contacts_list.append(list(result.groups()))
        if new_contacts_list[i][0] in new_contacts_list:
            print(new_contacts_list[i][0:3])
        if new_contact_list[i][5] != None:
            new_contacts_list[i][5] = phone_pattern.sub(r'+7(\2)\4-\6-\7 \10\11', new_contacts_list[i][5])


final_contact_list = []
for i in range(len(new_contact_list)):
    for a in range(len(new_contact_list)):
        if new_contact_list[i][0] == new_contact_list[a][0]:
            new_contact_list[i] = [x or y for x, y in zip(new_contact_list[i], new_contact_list[a])]
            if new_contact_list[i] not in final_contact_list:
                final_contact_list.append(new_contact_list[i])
pprint(final_contact_list)


with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts_list)
