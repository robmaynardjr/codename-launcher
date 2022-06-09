from hashlib import new
from msilib.schema import Class
from typing_extensions import Self
from azure.containerregistry import ContainerRegistryClient
from azure.cli.core import get_default_cli

class Create_ACR():     
    # Create Registry
    def create_acr(Self.acr_url, region, replication, sku, admin):
        Self.acr_url = input("tst")
        region = ('')
        replication = bool
        eplication_region = repl_region
        sku = ("")
        admin = bool        
        if exit_code == 0:
            print ("ACR created")
        else: 
            print(logs)

createAcr = ACR.create_acr('maynard1', 'centralus', False, 'Standard', True)