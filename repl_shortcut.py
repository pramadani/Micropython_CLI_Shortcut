# softreset
import machine; machine.reset()

# run file
exec(open('main.py').read())

# list file
import os; [print(item) for item in os.listdir('/')]

# read file
print(open('main.py', 'r').read())

# remove file
import os; os.remove('main.py')