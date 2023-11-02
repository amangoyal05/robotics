import os

os.chdir('D:/Coding/robotics/img')
print(os.getcwd())

for f in os.listdir():
    # print(f)
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_number = f_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip() 
    f_number = f_number.strip()[1:].zfill(2)
    # print(f'{f_number}-{f_course}-{f_title}{f_ext}')
    new_name = f'{f_number}-{f_course}-{f_title}{f_ext}'
    os.rename(f, new_name)
    print(new_name)