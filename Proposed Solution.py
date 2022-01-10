import os
import time
f_names = open('venv/teste_cases/names_case4.txt', 'r')
fs_names = f_names.readlines()
fs_names = [x.replace('\n', '') for x in fs_names]
f_phones = open('venv/teste_cases/phones_case4.txt', 'r')
fs_phones = f_phones.readlines()
fs_phones = [x.replace('\n', '') for x in fs_phones]
f_emails = open('venv/teste_cases/emails_case4.txt', 'r')
fs_emails = f_emails.readlines()
fs_emails = [x.replace('\n', '') for x in fs_emails]
def organizer(ff_names,ff_phones,ff_emails):
    x=[]
    y=[]
    if ff_names == [] or ff_phones == [] or ff_emails == []:
        return print('Error one or more files are empty')
    elif len(ff_names) != len(ff_phones) or len(fs_names) != len(ff_emails) or len(ff_phones) != len(ff_emails):
        return print('Error the number of inputs does not mach')
    else:
        for i in range(len(ff_names)):
            if len(ff_phones[i]) > 11 or len(ff_phones[i]) < 11:
                return print('Error the phone number', ff_phones[i], 'have a invalid number of digits')
            elif any(char.isdigit() for char in fs_names[i]):
                return print('Error the name',ff_names[i],'contain a number')
            else:
                x.append([ff_names[i]] + [ff_phones[i]] + [ff_emails[i]])
        for y in range(len(x)):
            for j in range(0,len(x) - y - 1):
                if x[j] > x[j+1]:
                    x[j],x[j+1] = x[j+1],x[j]
    return print(x)
f_names.close()
f_phones.close()
f_emails.close()
t1 = time.time()
organizer(fs_names,fs_phones,fs_emails)
t2 = time.time()
print('running time is',t2-t1)