#!/usr/bin/env python3
import os
from app.views import *

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
