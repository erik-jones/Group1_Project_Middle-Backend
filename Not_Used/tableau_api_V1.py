import pandas as pd

from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_views_dataframe, get_view_data_dataframe
from tableau_api_lib.utils import flatten_dict_column
from tableau_api_lib.utils.querying import get_sites_dataframe

SITE_NAMES = None

#Personal Access Token
#Token Name: test_token
#Token Secret: C8uI/8q1RaqsDIZTQFDz6Q==:kkgMqOEcyguTCMuyIrX0EspnG5jNhLhm

DB_SERVER_QUERY = """
{
    databaseServers {
        name
        hostName
        port
        connectionType
        isEmbedded
    }
}"""

DATA_CONNECTIONS_QUERY = """
{
    databases {
        name
        __typename
        connectionType
    }
}"""

tableau_server_config = {
        'my_env': {
                'server': 'https://prod-useast-a.online.tableau.com/',
                'api_version': '3.15',
                # 'username': '<YOUR_USERNAME>',
                # 'password': '<YOUR_PASSWORD>',
                'personal_access_token_name': 'test_token',
                'personal_access_token_secret': 'C8uI/8q1RaqsDIZTQFDz6Q==:kkgMqOEcyguTCMuyIrX0EspnG5jNhLhm',
                'site_name': 'uamgtdataviz',
                'site_url': 'uamgtdataviz'
        }
}
conn = TableauServerConnection(tableau_server_config, env='my_env')
conn.sign_in()

sites_df = get_views_dataframe(conn)


db_servers_df = pd.DataFrame()
data_connections_df = pd.DataFrame()

for index, site in sites_df.iterrows():
    conn.switch_site(site['contentUrl'])
    response_a = conn.metadata_graphql_query(DB_SERVER_QUERY)
    response_b = conn.metadata_graphql_query(DATA_CONNECTIONS_QUERY)
    site_db_servers_df = pd.DataFrame(response_a.json()['data']['databaseServers'])
    site_data_connections_df = pd.DataFrame(response_b.json()['data']['databases'])
    site_db_servers_df['site_name'] = site['name']
    site_data_connections_df['site_name'] = site['name']
    db_servers_df = db_servers_df.append(site_db_servers_df, sort=False, ignore_index=True)
    data_connections_df = data_connections_df.append(site_data_connections_df, sort=False, ignore_index=True)
    
combined_db_df = data_connections_df.merge(db_servers_df, how='left', on=['name', 'connectionType', 'site_name'])
combined_db_df_unique = combined_db_df.drop(columns=['name', 'site_name']).drop_duplicates()
print(views_df.to_string())