server_setup
============

a list of scripts that will be used to setup servers


This purpose of this project is to allow you to quickly build a server environment for either your development or production needs, using the following development stack :

* Rails 4
* RVM
* Nginx
* MySQl
* Ubuntu >= 14.04


### Server Types

* development
  * Rails via RVM
  * MySQL Server AND client
* webserver
  * Rails via RVM
  * MySQL client
  * a deployment user (called deployer)
  * nginx
* sqlserver
  * MySQL client
  * 
 
### Quick Download
```bash
sudo apt-get update
sudo apt-get install unzip
wget https://github.com/cjbuchmann/server_setup/archive/master.zip
unzip master.zip
```

### Usage

Setup a development server (Install MySQl server and client, and rails 4)
```bash
./setup.py -e development
```

Setup a development server and create git config author settings. Also generate an ssh key (using the git config email)

```bash
./setup.py -e development -wgc -gcname "John Doe" -gcemail "email@example.com" -sshkeygen
```

Setup a production webserver
```bash
./setup.py -e webserver
```

Setup a database server
```bash
./setup.py -e sqlserver
```
