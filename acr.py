from hashlib import new
from msilib.schema import Class
from azure.containerregistry import ContainerRegistryClient
from azure.cli.core import get_default_cli

class Create_ACR:
     
    # Create Registry
        def create_acr(acr_name, region, replication, sku, admin):
            region = ('az account list-locations -o table')
            acr_name = input("")
            region = ()
            replication = bool
            replication_region = repl_region
            sku = ("")
            admin = bool        
            if exit_code == 0:
                print ("ACR created")
            else: 
                print(logs)


createAcr = ACR.create_acr('maynard1', 'centralus', False, 'Standard', True)