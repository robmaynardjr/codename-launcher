from hashlib import new
from msilib.schema import Class
from typing_extensions import Self
from azure.containerregistry import ContainerRegistryClient
from azure.cli.core import get_default_cli
from az.cli import az

class Create_ACR:
        
        # Create Registry
        def create_acr(acr_url, acr_region, replication, replication_region, sku, admin):
            acr_url = input("tst")
            replication = input(bool)
            replication_region = input(repl_region)
            sku = input("")
            admin = input(bool)
            acr_region = input('')
            args=[acr_url, replication, replication_region, sku, admin, acr_region]
            cli = get_default_cli()
            if cli.invoke(args):
                return cli.result.result
            elif cli.result.error:
                raise cli.result.error
            return True    
            