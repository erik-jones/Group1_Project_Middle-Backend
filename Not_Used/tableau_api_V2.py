import tableauserverclient as TSC

#Personal Access Token
#----------------------
#Token Name: test_token
#Token Secret: C8uI/8q1RaqsDIZTQFDz6Q==:kkgMqOEcyguTCMuyIrX0EspnG5jNhLhm
#Final updates: Test tokens no longer work

tableau_auth = TSC.PersonalAccessTokenAuth('test_token', 'C8uI/8q1RaqsDIZTQFDz6Q==:kkgMqOEcyguTCMuyIrX0EspnG5jNhLhm', 'uamgtdataviz')
server = TSC.Server('https://prod-useast-a.online.tableau.com/', use_server_version=True)
server.auth.sign_in(tableau_auth)

#Displays all the data sources from Tableau online
#The name of the data source is matched with the index of it's id
#E.g: 'Database(EL Database)' is at [1] so the id at [1] is the id for 'Database(EL Database)'
with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    print([datasource.name for datasource in all_datasources])
    print([datasource.id for datasource in all_datasources])

#Validating the name of the source
with server.auth.sign_in(tableau_auth):
    datasource = server.datasources.get_by_id('ddc2b755-11db-4209-9616-260531ed9774')
    print(datasource.name)

#Testing the source by downloading the file (NO PERMISSION)
with server.auth.sign_in(tableau_auth):
  file_path = server.datasources.download('ddc2b755-11db-4209-9616-260531ed9774')
  print("\nDownloaded the file to {0}.".format(file_path))

server.auth.sign_out()