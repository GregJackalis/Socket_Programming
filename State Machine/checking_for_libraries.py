# In case on my assignment files I use an external python library that in order for my program to work
# it needs to be installed, then I use the code below to check if the library is already installed in the machine
# the program is running in, and if not the script will install it automatically

try:
    import statemachine
    print("Library is already installed inside this machine, it's imported succesfully!")
except ImportError:
    print("python-statemachine not found. Installing...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'python-statemachine'])
    print("Library installed successfully.")
    
# Now you can use the library without any issues
try:
    import statemachine
    print("Library installed succesfully in this machine!")
except ImportError:
    print("There was a problem pip-installing and importing the libary.")


try:
    import pydot
    print("Library is already installed inside this machine, it's imported succesfully!")
except ImportError:
    print("pydot library not found. Installing...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'pydot'])
    print("Library installed successfully.")
    
# Now you can use the library without any issues
try:
    import pydot
    print("Library installed succesfully in this machine!")
except ImportError:
    print("There was a problem pip-installing and importing the libary.")