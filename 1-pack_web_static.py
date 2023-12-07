#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Creates a .tgz archive from web_static folder
    """
    try:
        # Create the 'versions' directory if it doesn't exist
        local("mkdir -p versions")

        # Generate the timestamp for the archive name
        time_format = "%Y%m%d%H%M%S"
        timestamp = datetime.utcnow().strftime(time_format)

        # Create the archive using tar command
        archive_name = "web_static_{}.tgz".format(timestamp)
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if created successfully
        archive_path = "versions/{}".format(archive_name)
        print("Archive created at:", archive_path)
        return archive_path

    except Exception as e:
        print("Error:", str(e))
        return None

if __name__ == "__main__":
    do_pack()
