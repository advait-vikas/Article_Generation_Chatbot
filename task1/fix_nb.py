import nbformat
import os

def fix_widgets_metadata(filename):
    nb = nbformat.read(filename, as_version=nbformat.NO_CONVERT)
    if 'widgets' in nb['metadata']:
        if 'state' not in nb['metadata']['widgets']:
            print(f"Fixing: {filename}")
            del nb['metadata']['widgets']
            nbformat.write(nb, filename)

def walk_and_fix_notebooks(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.ipynb'):
                fix_widgets_metadata(os.path.join(root, file))

if __name__ == "__main__":
    # Change '.' to your notebooks directory if needed
    walk_and_fix_notebooks('.')