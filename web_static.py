import os.path
from datetime import datetime
from fabric.api import local


def create_compressed_archive():
    """Create a compressed archive (.tgz) of the web_static directory."""
    current_time = datetime.utcnow()
    archive_filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        current_time.year,
        current_time.month,
        current_time.day,
        current_time.hour,
        current_time.minute,
        current_time.second
    )

    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None

    if local("tar -cvzf {} web_static".format(archive_filename)).failed:
        return None

    return archive_filename
