
import sys
import os
import stat



if __name__ == '__main__':
    script_name = sys.argv[0]
    file_path = sys.argv[0]  # or any file

    print("Script name:", script_name)

    # Get current mode
    mode = os.stat(file_path).st_mode
    print("Current permissions:", stat.filemode(mode))

    # Add executable permission for owner and group
    new_mode = mode | stat.S_IXUSR | stat.S_IXGRP
    new_mode = new_mode & ~stat.S_IXOTH

    os.chmod(file_path, new_mode)

    # Verify
    mode_after = os.stat(file_path).st_mode
    print("New permissions:", stat.filemode(mode_after))