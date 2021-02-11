#!/usr/bin/env python

import hashlib
import sys

given_str = sys.argv[1].encode("utf-8")
print(hashlib.md5(given_str).hexdigest())
