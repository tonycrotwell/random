#!/bin/bash

##Check to ensure script is run by root user!

if [ "$EUID" -ne 0 ]
  
    then echo "Script must be run as root, please re-run as root user"
  
   exit

else

#Grab variables

DOMAIN=$(whiptail --title "Domain Input Form" --inputbox "What is your Active Directory Domain?" 10 60  3>&1 1>&2 2>&3)

ADMINUSER=$(whiptail --title "Admin User Form" --inputbox "What is your Administrative User Name?" 10 60  3>&1 1>&2 2>&3)

##See if WGET is installed and if not, install it

if ! yum list installed | grep wget

   then
    
     yum install -y wget

   fi
#Grab the repo file

wget -O /etc/yum.repos.d/pbiso.repo http://repo.pbis.beyondtrust.com/yum/pbiso.repo

#Install PBIS Software

yum install -y pbis-open pbis-open-upgrade

#Configure PBIS for Domain

/opt/pbis/bin/domainjoin-cli join $DOMAIN $ADMINUSER

/opt/pbis/bin/config AssumeDefaultDomain true

/opt/pbis/bin/config LoginShellTemplate "/bin/bash"

/opt/pbis/bin/config SpaceReplacement "_"

#Set up sudoers

echo "%domain_admins  ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers

  fi
exit 0
