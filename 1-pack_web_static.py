from fabric.api import local
from datetime import datetime

def do_pack():
    # Create a compressed archive of the web_static folder and save it in the versions directory
    # The archive name should include the current date and time
    # Return the archive path if the archive was generated correctly, otherwise return None
    
    # Check if the versions directory exists, create it if it doesn't
    if not local("test -d versions").succeeded:
        local("mkdir versions")
    
    # Get the current date and time for the archive name
    now = datetime.now()
    archive_name = "web_static_{0.year}{0.month:02d}{0.day:02d}{0.hour:02d}{0.minute:02d}{0.second:02d}.tgz".format(now)
    
    # Use tar command to create the archive
    result = local("tar -czf versions/{} web_static".format(archive_name))
    
    # Check if the archive was generated successfully and return the archive path or None
    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None

