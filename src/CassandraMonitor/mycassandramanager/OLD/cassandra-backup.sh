#!/bin/sh

# Variables
NODETOOL='/usr/bin/nodetool -h localhost'
CASSPATH='/home/cassandra08/data/'
CASSBACKUP='/home/cassandra-backup'
CASSTEXT='/root/cass-backup.txt'
TAR='/bin/tar'
GZIP='/bin/gzip'
RM='/bin/rm'
MAIL='/bin/mail'

# Remove old snapshots
$NODETOOL clearsnapshot

# Flush commits to disk
$NODETOOL flush

# Create new snapshots
$NODETOOL snapshot

# Remove old backups
$RM -f $CASSBACKUP/*.tar.gz

# Tar and Gzip snapshots for backup

for i in `find $CASSPATH -name snapshots`
 do
 x=${i/snapshots/}
 $TAR -cf $CASSBACKUP/`hostname -s`-`basename $x`.tar $i
 $GZIP $CASSBACKUP/*.tar
done

# scp to Shep for backup to Bacula
scp -P48522 -p /home/cassandra-backup/* root@int.shep:/home/cassandra-backup/

# Remove old snapshots
$NODETOOL clearsnapshot

ls -lh $CASSBACKUP > $CASSTEXT
#$MAIL -s "`hostname -s`-Cassandra-Backup" WebMonitoring@hf-uk.com < $CASSTEXT

$MAIL -s "`hostname -s`-Cassandra-Backup" webmonitoring@hf-uk.com < $CASSTEXT

