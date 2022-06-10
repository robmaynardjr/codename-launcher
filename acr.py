from hashlib import new
from msilib.schema import Class
from typing_extensions import Self
from azure.containerregistry import ContainerRegistryClient
from azure.cli.core import get_default_cli
from az.cli import az

class Create_ACR:
        acr_url = input("tst")
        replication = bool
        replication_region = repl_region
        sku = ("")
        admin = bool
        acr_region = input('')
        # Create Registry
                
        def create_acr(acr_url, acr_region, replication_region, sku, admin): 
                     
            if exit_code == 0:  
                print ("ACR created")
            else: 
                print(logs)