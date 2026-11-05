# Use mbox-short.txt as the file name
try:
    file = input('Enter file: ')
    text = open(file)
except:
    print('Error file name!')
result_time = dict()
count_time = dict()
for line in text:
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        line_time = words[5]

        time = line_time.split(":")
        time = time[0]
        count_time[time] = count_time.get(time, 0) + 1

        # print(time[0])

        #person = words[1]

        #count_email[person] = count_email.get(person, 0) + 1
for k, v in sorted(count_time.items()):
    print(k, v)