from .base import *  # noqa:403

ROOT_DIR = os.path.dirname(BASE_DIR)  # noqa 405
STATIC_ROOT = os.path.join(ROOT_DIR, "static")
MEDIA_ROOT = os.path.join(ROOT_DIR, "media")
DEBUG = False
