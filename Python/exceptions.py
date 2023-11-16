try:
    f = open('currupt_file.txt', 'r')
    if f.name == 'currupt_file.txt':        # Manually creating an error
        raise Exception
    # var = bad_var
except FileNotFoundError as e:
    # print('Sorry. This file does not exist')
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:                                    # This will run no matter what
    print("Executing Finally...")

print('End File')