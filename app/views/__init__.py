

from app.views.users import *
from app.views.patients import *
from app.views.diseases import *


@app.route('/')
def index():
    return render_template('index.html')