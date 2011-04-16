import sys, os
sys.path.append(os.path.dirname( os.path.realpath(os.path.realpath( __file__ ) + '/../../' ) ))
from MiniMVC.Service import Service

class ServicesSectionLoader:

    def load(self, container, config):
        
        for name in config:
            
            service_def = config[name]
            
            if not 'class' in service_def:
                return False
                
            if 'params' in service_def:
                params = service_def['params']
            else:
                params = []
                
            service = Service(service_def['class'], params)
            container.set_service(name, service)

        return True