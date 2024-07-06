#!/usr/bin/python3
"""
generate a .tgz archive
"""

from datetime import datetime
from fabric.api import local
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """
 The function's purpose is to create a .tgz archive from web_static folder.
    """

    local("mkdir -p versions")
    date_format = "%Y%m%%d%H%M%S"
    archive_path = "versions/web_static_{}.tgz".format(
            datetime.strftime(datetime.now(), date_format))
    result = local("tar -cvzf {} web_static".format(archive_path))
    if result.failed:
        return None
    return archive_path

