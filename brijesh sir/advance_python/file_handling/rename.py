from datetime import datetime

def generate_unique_id(postStr):
    current_time = datetime.now()
    dateStr = datetime.strftime(current_time, '%d%m%Y-%H%M%S-%f_')
    unique_id = dateStr + postStr
    return unique_id

import os

os.rename('brijesh.jpg', str(generate_unique_id('profile')) + '.jpg')