from hashlib import new
from msilib.schema import Class
from typing_extensions import Self
from azure.containerregistry import ContainerRegistryClient
from azure.cli.core import get_default_cli

class Create_ACR(acr_url, acr_region, replication, sku, admin):
        # Create Registry
    def create_acr(acr_url, region, replication, sku, admin):
        
        self.acr_url = input("tst")
        self.acr_region = ('')
        self.replication = bool
        self.eplication_region = repl_region
        self.sku = ("")
        self.admin = bool
        if exit_code == 0:
            print ("ACR created")
        else: 
            print(logs)

createAcr = create_acr('maynard1', 'centralus', False, 'Standard', True)