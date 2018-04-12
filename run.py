#!/usr/bin/env python3
import os
from app.errors import *
from app.views import *

app.secret_key = os.urandom(12)

if __name__ == '__main__':
    app.run(debug=True)
