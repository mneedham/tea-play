#!/usr/bin/env python

"""
---
dependencies:
  python.org: 3.10.8
---
"""

import platform
import json

print(json.dumps({"Version": platform.python_version()}))