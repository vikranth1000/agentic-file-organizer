import os

def scan_folder(folder_path):
    """
    Recursively scans folder and returns:
    - A list of all visible (non-hidden) file paths
    - A list of all visible (non-hidden) folder paths
    """
    file_paths = []
    folder_paths = []
    for root, dirs, files in os.walk(folder_path):
        # Filter out hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for d in dirs:
            folder_paths.append(os.path.join(root, d))
        # Filter out hidden files
        visible_files = [f for f in files if not f.startswith('.')]
        for f in visible_files:
            file_paths.append(os.path.join(root, f))
    return file_paths, folder_paths
