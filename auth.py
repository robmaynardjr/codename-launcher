from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient
from pysmartthings import Subscription
import acr

credential = DefaultAzureCredential()
#Gather subscriptions
client = ResourceManagementClient(
    credential=credential,
    subscription_id=input("acr.subscription")
# Gather resource groups
for resource_group in Subscription.list():
    print(f"Resource group: {resource_group.name}")
# Not sure if needed
return(f"Successful credential: {credential._successful_credential.__class__.__name__}")