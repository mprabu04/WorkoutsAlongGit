import sys
"""Print function learning to possible extent"""

"""Test Print function with complete arguments """
print('sample','test', sep=' ', end='\n', file=sys.stdout, flush=False)

"""Test Print function with file parameter"""
sourceFile = open('python.txt', 'w')
print('sample test', file=sourceFile)
print('hello, world', file=sourceFile)
sourceFile.close()


"""Test to Print blank lines"""

print(8 * '\n')  # instead of print('\n\n\n\n\n\n\n\n')
print()
print()

"""Test to Print with other end keyword value"""

print('Python', end='@')

