from azure.identity import DefaultAzureCredential
from azure.identity import AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential
class auth:
    
    def config_creds():
        default_credential = DefaultAzureCredential()
        DefaultAzureCredential(exclude_interactive_browser_credential=False)
        DefaultAzureCredential(managed_identity_client_id=client_id)
        managed_identity = ManagedIdentityCredential()
        azure_cli = AzureCliCredential()
        credential_chain = ChainedTokenCredential(managed_identity, azure_cli)
        client = EventHubProducerClient(namespace, eventhub_name, credential_chain)
        
        credential = DefaultAzureCredential()
        credential = DefaultAzureCredential()
        async wiht credentials
        
        