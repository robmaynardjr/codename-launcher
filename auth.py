from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient

credential = DefaultAzureCredential()

client = ResourceManagementClient(
    credential=credential,
    subscription_id=input("subscription")

for resource_group in client.resource_groups.list():
    print(f"Resource group: {resource_group.name}")

print(f"Successful credential: {credential._successful_credential.__class__.__name__}")