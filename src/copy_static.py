import os
import shutil

def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    os.mkdir(dst)
    items = os.listdir(src)
    
    for item in items:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {src_path} to {dst_path}")
        else:
            # Create the directory in destination
            os.mkdir(dst_path)
            # Recursively copy contents of this directory
            copy_static(src_path, dst_path)
            print(f"Copied directory: {src_path} to {dst_path}")