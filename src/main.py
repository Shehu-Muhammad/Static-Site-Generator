import os
import shutil
from copy_static import copy_static
from generate_pages_recursive import generate_pages_recursive

def main():
    # Remove public directory and its contents if it exists
    if os.path.exists("public"):
        shutil.rmtree("public")
    
    # Create fresh public directory
    os.makedirs("public")
    
    # Copy static files - pass both src and dst arguments
    copy_static("static", "public")
    
    # Generate the index page
    generate_pages_recursive(
        "content",  # content_dir
        "template.html",  # template_path
        "public"    # public_dir
    )

if __name__ == "__main__":
    main()