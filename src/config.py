import os
from dotenv import load_dotenv

load_dotenv()

# Table configuration with defaults
TABLE_WIDTH = int(os.getenv('TABLE_WIDTH', 5))
TABLE_HEIGHT = int(os.getenv('TABLE_HEIGHT', 5))

# ensure minimum size is not less than 1
if TABLE_WIDTH < 1:
    TABLE_WIDTH = 5
if TABLE_HEIGHT < 1:
    TABLE_HEIGHT = 5 