import os

start_path = os.path.abspath(os.path.join('..', '..', os.path.curdir))
print('Start path: ', start_path)
for path, dirs, files in os.walk(start_path):
    # process directories
    for name in dirs:
        print("Directory: {}".format(os.path.join(path, name)))

    # process files
    for name in files:
        print("File: {}".format(os.path.join(path, name)))