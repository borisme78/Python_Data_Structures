# Use mbox-short.txt as the file name
try:
    file = input('Enter file: ')

    text = open(file)
except:
    print('Error file name!')

count_email = dict()
for line in text:
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        person = words[1]
    
        count_email[person] = count_email.get(person, 0) + 1

#print(count_email)
name_email = None
count_max_email = None

for email, count in count_email.items():
    if count_max_email is None or count > count_max_email:
        name_email = email
        count_max_email = count

print(name_email, count_max_email)