import os
import sys
import shutil
from copy_static import copy_static
from generate_pages_recursive import generate_pages_recursive

def main():
    # Get the basepath from the command line arguments
    basepath = "/" # Default value
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    # Use 'docs' directory instead of 'public'
    output_dir = "docs"

    # Remove public directory and its contents if it exists
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    # Create fresh public directory
    os.makedirs(output_dir)
    
    # Copy static files - pass both src and dst arguments
    copy_static("static", output_dir)
    
    # Generate the index page
    generate_pages_recursive(
        "content",        # content_dir
        "template.html",  # template_path
        output_dir,       # public_dir -> now using docs instead
        basepath          # adding the basepath parameter here
    )

if __name__ == "__main__":
    main()