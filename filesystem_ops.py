import os
from pathlib import Path

for itm in Path.iterdir(Path.cwd()):
    print(f"File:{itm}")

