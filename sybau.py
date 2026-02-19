#!/usr/bin/env python3

import sys
import subprocess

val = subprocess.run(sys.argv[1:], capture_output=True, text=True)

if val.returncode != 0:
    print("Failure")
    output = val.stderr.strip() or val.stdout.strip()
    if output:
        print(output)
    sys.exit(val.returncode)
else:
    print("Successfully completed")   
