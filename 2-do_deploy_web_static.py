#!/usr/bin/python3
"""
Distributing an archive to my web servers,
using the function do_deploy
"""
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['54.175.189.228', '54.237.217.95']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Deploying archive to web server
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to each server in the env.hosts list
        for host in env.hosts:
            put(archive_path, '/tmp', use_sudo=True)

            # Extract the archive into a unique folder
            archive_filename = os.path.basename(archive_path)
            archive_folder = '/data/web_static/releases/{}'.format(
                archive_filename.split('.')[0])
            run('mkdir -p {}'.format(archive_folder))
            run('tar -xzf /tmp/{} -C {}'.format(archive_filename, archive_folder))

            # Delete the uploaded archive from the /tmp directory
            run('rm /tmp/{}'.format(archive_filename))
            # Remove existing files in target directories
            run('rm -rf {}/web_static/images/*'.format(archive_folder))
            run('rm -rf {}/web_static/styles/*'.format(archive_folder))
            run('mkdir -p {}/web_static/images'.format(archive_folder))
            run('mkdir -p {}/web_static/styles'.format(archive_folder))
            # Move only the files from the web_static directory
            run('mv -f {}/web_static/* {}'.format(archive_folder, archive_folder))

            # Remove the now-empty web_static folder
            run('rm -rf {}/web_static'.format(archive_folder))

            # Update the symbolic link
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(archive_folder))

        print('New version deployed!')
        return True
    except Exception as e:
        print('Error deploying:', str(e))
        return False

