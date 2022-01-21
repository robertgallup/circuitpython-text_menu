# Simple menu generator for CircuitPython
#
# Lists all python files (.py) except main.py, code.py,
# or anything that begins with "." or "_"
# Each file is preceded by a letter
# Typing a letter followed by <return> will launch the
# corresponding program
#
# To exit and restart the menu, <ctrl+c>, <ctrl+d>

import supervisor
import os
import sys
import time

# True runs the first program after timeout, False disables timeout
TIMEOUT = False
# Number of seconds to wait for timeout
TIMEOUT_SECONDS = 10.0
# Allowed extensions
ALLOWED_EXTENSIONS = {'txt', 'py', 'mpy'}
# Ignored names
IGNORED_NAMES = {'code', 'main', 'boot_out'}
# Number of nanoseconds to wait for timeout. (10**9 = 1,000,000,000) converts seconds to nanoseconds.
TIMEOUT_TIME = TIMEOUT_SECONDS * (10**9)

# Check file name against allowed extensions
def type_allowed (f, ext_list):
	return f.rpartition('.')[2] in ext_list

# Check file name against allowed names
def name_ignored (f, name_list):
	return f.rpartition('.')[0] in name_list

# Get the sorted list of directory contents
ls = sorted(os.listdir())
# First menu character
c = ord('a')
# Last possible menu character
max_char = ord('z')
# Dictionary of choices
choices = {}
last_choice = ''
more = False
# For each item in the directory
for f in ls:
	# Skip leading period and underscore
	if(f[0] == '.' or f[0] == '_'):
		continue
	# Skip anything that doesn't have an allowed extension
	elif (not type_allowed(f, ALLOWED_EXTENSIONS)):
		continue
	# Skip main.py and code.py
	elif (name_ignored(f, IGNORED_NAMES)):
		continue
	# Passed the gauntlet, so record the file
	else:
		last_choice = chr(c)
		choices[last_choice] = f
		c += 1
		if (c > ord('z')):
			more = True
			break

# List the choices
print()
for f in sorted(choices):
	print (f+'.', choices[f])
if more:
	print("more...")

# And, a prompt
print (f"\nChoose[a-{last_choice}]: ", end='')
value = ""
time_start = time.monotonic_ns()
# Wait for input or timeout:
while True:
	time.sleep(.1)

	# Time out
	if TIMEOUT and ((time.monotonic_ns() - time_start) > TIMEOUT_TIME):
		value = 'a'
		print("timeout")

	elif supervisor.runtime.serial_bytes_available:
		value = input().strip()
	else:
		continue

	# Ignore spurious newlines
	if value == "":
		continue
	# If the value isn't valid, say so
	if value not in choices:
		print ("Unrecognized choice...\n\nChoose: ", end='')
	# Valid choice, so run module
	else:
		print (f"Running: ", choices[value], "\n")
		c = choices[value]
		supervisor.set_next_code_file (c)
		supervisor.reload()

