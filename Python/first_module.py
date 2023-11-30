# Whenever a python code is run, it always creates special variables that have initial values.
# __name__ is one of those special variables.
# When python runs the program directly, the value of name is equal to the main 

print("This will always be run")

def main():
    # print(f"First Module's Name: {__name__}")
    print(f"First Module's Main Method")
    
# This is basically a check to see if Python is directly running this file or is it being imported
if __name__ == '__main__':
    main()
#     print("Run Directly")
# else:
#     print("Run From Import")