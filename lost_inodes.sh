 #! /bin/sh
# Compliments of Jamie Miler #
#If a system loses power during a large write you may have disconnected inodes with file headers
#this script will find and attach those back together.
 
src=/opt1/pf_dbs/lost+found
dst=/opt1/pf_dbs/SAFE/2001_split
 
cd $dst
ls -1i > /var/tmp/junk.$$
tot=`cat /var/tmp/junk.$$|wc -l|tr -d ':[space]:'`
c=1
 
while [ $c -le $tot ];
do
        inode=`head -$c /var/tmp/junk.$$|tail -1|awk '{print $1}'`
        file=`head -$c /var/tmp/junk.$$|tail -1|awk '{print $2}'`
        mv $src/#$inode $dst/$file
        c=`expr $c + 1`
done
