'''
detcordRevTool : Action execution on hosts
Micah Martin - knif3
Shannon McHale - LittleHack3r
'''

from detcord import action, display

env = {}  # pylint: disable=invalid-name
env['user'] = 'root'
env['pass'] = 'toor'
env['hosts'] = ['localhost']
env['threading'] = False  # threading defaults to false

@action
def deployRevTool(host):
    
    try:
        host.put("/Users/loveofmyfuckinglifewow/Tools/RevTool.py", "/tmp/RevTool.py")
        ret = host.run("python3 /tmp/RevTool.py")
        
    
    except PermissionError as _:
        # Catch a permission denied error and try again as root
        host.put("/Users/loveofmyfuckinglifewow/Tools/RevTool.py", "/tmp/README", sudo=True)

def support_action():
    '''
    This function is not a detfile action and cannot be called with det
    '''
    pass