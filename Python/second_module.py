# Importing the first_module will cause Python to execute it.first_module
# Here the name variable will be set to first_module as it is not run directly.
import first_module

first_module.main()

print(f"Second Module's Name: {__name__}")