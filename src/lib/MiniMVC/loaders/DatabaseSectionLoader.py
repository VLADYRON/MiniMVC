import sys, os
sys.path.append(os.path.dirname( os.path.realpath(os.path.realpath( __file__ ) + '/../../' ) ))
from MiniMVC.orm.ORM import ORM

class DatabaseSectionLoader:

    def load(self, container, config):
        
        if not 'type' in config or not 'host' in config or not 'user' in config or not 'password' in config or not 'database' in config:
            return False
            
        orm = ORM(config['type'], config['host'], config['user'], config['password'], config['database'])
        container.set_param('sys.orm', orm)