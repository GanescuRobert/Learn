
try:
    g = open('my_text.txt','w')
except FileNotFoundError as error:
    print(error)
else:
    while True:
        user_input = input('Enter student records in one line (q to quit): ')
        user_input = user_input + '\n'
        if user_input == 'q\n':
            break
        g.write(user_input)
    g.close()
finally:
    print('Write, program is closed!')
    
try:
    f = open('my_text.txt','r')
except FileNotFoundError as error:
    print(error)
else:
    record_list = f.readlines()
    f.close()
    for record in record_list:
        print(record)
finally:
    print('Read, program is closed')