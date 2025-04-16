from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

OCTOPUS_ENERGY_GRAPHQL_ENDPOINT = r'https://api.octopus.energy/v1/graphql/'

transport = RequestsHTTPTransport(
    url=OCTOPUS_ENERGY_GRAPHQL_ENDPOINT,
    verify=True,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql(
    """
"""
)

result = client.execute(query)
print(result)