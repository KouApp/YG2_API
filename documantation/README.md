# key
git clone https://yasinsahin0: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@github.com/KouApp/yaz1Api.git  
git clone https://yasinsahin0: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@github.com/KouApp/yaz1Api.git  

## Could not get lock /var/lib/dpkg/lock-frontend - open (11: Resource temporarily unavailable) [duplicate]

'Synaptic Package Manager' or 'Software Updater' is open.  
Some apt command is running in Terminal.  
Some apt process is running in background.  
For above wait for the process to complete. If this does not happen run in terminal:  
 
sudo killall apt apt-get  
If none of the above works, remove the lock files. Run in terminal:  

sudo rm /var/lib/apt/lists/lock  
sudo rm /var/cache/apt/archives/lock  
sudo rm /var/lib/dpkg/lock*  
then reconfigure the packages. Run in terminal:  
  
sudo dpkg --configure -a  
and  
 
sudo apt update  




## sql hatası

https://github.com/mkleehammer/pyodbc/issues/938

odbc kurulumu
sudo su
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list  
exit  
sudo apt-get update  
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17  
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools  
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc  
source ~/.bashrc  
sudo apt-get install -y unixodbc-dev  
