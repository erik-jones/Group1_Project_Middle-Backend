import pysftp

#Setting up server connections
Hostname = "sftp.wp.com"
Username = "uacel.wordpress.com"
Password = "fFa5C4yemMFA6zy9eCJE" #if needed, change this

#ensures that you don't need a "host key" in order to connect to a server
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

#This connects you to the root directory which is "htdocs" (you can see this folder via FileZilla)
with pysftp.Connection(host=Hostname, username=Username, password=Password,port=22,cnopts=cnopts) as sftp:

    print("Connection successfully established ... ")
    # Switch to a remote directory

    sftp.cwd('data')

    # Obtain structure of the remote directory 'data'
    directory_structure = sftp.listdir_attr()

    # Print data
    for attr in directory_structure:
        print(attr.filename, attr)