# Group1_Project_Middle-Backend
* ## Project code for capstone project Spring 2022
  * ### Backend data collection for Engaged learning opportunites live
  * ### Pulls data from bamapulse using their api, writes that data to an excel file stored in box
<br></br>
* ## How to Run:
  *  All files being used are in the Data_Collection_Script folder

  *  Execution begins in 'Main.py', which calls all of the other files as needed

  *  To work, you need to add the proper values to 'Info.json'
     *  "givepulse_key" and "givepulse_secret":
        *  Follow the documentation at: https://bama.givepulse.com/api/group/
  
        *  These values need to be provided by someone with administrator access to givepulse, the documentation above has steps on how they can provide those under the 'Overview' section
  
     *  "givepulse_email" and "givepulse_password":
        * Can be any valid givepulse account
    <br></br>

     *  "box_file_id":
        *  Can be obtained by opening the excel file within box and checking the url. For example, for the url: https://alabama.app.box.com/file/9517, 9517 would be the file id. 
    <br></br>

     *  "box_client_id", "box_client_secret", "box_access_token":
        *  Documentation: https://github.com/box/box-python-sdk
  
        *  The documentation would be the best resource, but from my best understanding, you have to go to the box dev console (if you open box, there will be a link to it in the bottom left). Once this is open, you would create a new app, select "Custom App", then select "Server Authentication (Client Credentials Grant)"
  
        *  Once you've created the app you would then go to "Configuration" where about halfway down you can get the "Client ID" and "Client Secret"
  
        *  While on this page, towards the bottom under "App Access Level" select "App + Enterprise Access"
  
        *  Under "Application Scopes" select "Write all files and folders in Box"
  
        *  Under "Advanced Features" select "Generate user access tokens"
  
        *  Finally towards the top of the page under "Developer Token" select "Generate Developer Token" which will give you the value you need for "box_access_token"
<br></br>
* ## Improvements Needed:
  * Box access token:
    * The developer token only lasts about 60 minutes, then you have to manually generate a new one.
  
    * Moving foward a more permanent token will be needed. The documentation is once again the best resource for this, but to the best of my knowledge, under your app go to "Authorization" and request to have your app authorized.
  <br>
  * Security:  
    * Ideally would want a more secure way to store the values in "Info.json", we just were unable to get around to this in time
  <br></br>
  * Duplicate Check:   
    * In "WriteToExcel.py", need to add a way to check if an item is already in the file before adding it. We didn't have time to get around to this.
  
    * One possible solution would be to use the "sqlalchemy" and "pandas" libraries to create an sql statement (these libraries would allow you to do this on an excel file) to check if the unique id of an item is already in the file.
  <br></br>
  * Scheduled Script: 
    * Since this is for a university service, it would likely need to be hosted on a university server. Once on the server it should be set to run as a schedule job to check bamapulse for new updates.