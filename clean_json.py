import re
import os

path = r'c:\Users\vivie\Reporteportadas\data_portadas.json'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    with open(path, 'w', encoding='utf-8') as f:
        skip = False
        for line in lines:
            # We want to keep the "new" version (after =======) or just remove all markers and hope it's valid.
            # Usually, merge conflicts look like:
            # <<<<<<< HEAD
            # version A
            # =======
            # version B
            # >>>>>>> commit
            
            # Simple approach: remove lines starting with conflict markers.
            # This might leave some dangling commas or duplicate keys, but it's a start.
            if line.startswith('<<<<<<<') or line.startswith('=======') or line.startswith('>>>>>>>'):
                continue
            f.write(line)
    print("Conflict markers removed.")
else:
    print("File not found.")
