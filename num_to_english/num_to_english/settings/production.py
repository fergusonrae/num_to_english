
import os
from .base import *

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = [] # TODO: Add your production host here
