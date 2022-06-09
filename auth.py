from azure.identity import DefaultAzureCredent
from azure.mgmt.authorization import AuthorizationManagementClient
import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient

class auth:
    def authenticate(credentials):
        credentials = DefaultAzureCredential()
        