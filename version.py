#!/usr/bin/env python

"""
---
dependencies:
  python.org: 3.11.1
---
"""

import platform
import json

print(json.dumps({"Version": platform.python_version()}))