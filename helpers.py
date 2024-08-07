import os.path


def clear_screen():
    print("\n" * 100)


def delete_garb_files(file_path):
    """
    deletes files from a specific location

    Parameters:
        file_path (string): path to file
    :returns
        void
    """
    if os.path.exists(file_path):
        for file in os.listdir(file_path):
            os.remove(f"{file_path}/{file}")
