from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_views_dataframe, get_view_data_dataframe
from tableau_api_lib.utils import flatten_dict_column

#Personal Access Token
#Token Name: test_token
#Token Secret: C8uI/8q1RaqsDIZTQFDz6Q==:kkgMqOEcyguTCMuyIrX0EspnG5jNhLhm

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

views_df = get_views_dataframe(conn)
print(views_df.head())

views_df = flatten_dict_column(views_df, keys=["name","id"], col_name="workbook")
print(views_df)