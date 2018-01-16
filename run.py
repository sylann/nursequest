#!/usr/bin/env python3
from app import app
from app.views import *


if __name__ == '__main__':
    app.run(debug=True)
