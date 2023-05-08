#!/usr/bin/python3
"""Fabric script that generates a .tg archive from the contents of the
    web statics folder. ChatGPT generated code"""

from fabric.api import local, env, run
from datetime import datetime

env.hosts = ['localhost']
env.user = 'your_username'


def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder."""

    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_{}.tgz'.format(timestamp)

    local('mkdir -p versions')

    result = local('tar -czvf {} web_static'.format(archive_path))
    if result.failed:
        return None
    return archive_path
