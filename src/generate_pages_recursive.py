import os
from generate_page import generate_page

def generate_pages_recursive(content_dir, template_path, public_dir, basepath):
    items = os.listdir(content_dir)
    for item in items:
        current_path = os.path.join(content_dir, item)
        if os.path.isfile(current_path):
            if current_path.endswith('.md'):
                # 1. Create destination path (replace .md with .html)
                dest_path = os.path.join(public_dir, item.replace('.md', '.html'))
                # 2. Generate the page - passing the basepath here
                generate_page(current_path, template_path, dest_path, basepath)
        else:
            # 3. Handle directory case
            new_dest_dir = os.path.join(public_dir, item)
            # Make sure directory exists
            os.makedirs(new_dest_dir, exist_ok=True)
            # 4. Recursive call - passing the basepath here as well
            generate_pages_recursive(current_path, template_path, new_dest_dir, basepath)