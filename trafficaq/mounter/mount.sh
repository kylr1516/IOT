#!/bin/sh
#This is meant to download, mount, and retrive information from a sqsh file
read -p "Camera number: " CAMERA


# Making sure the proper directories exist
if ! test -e "$PWD/mnt"
then
mkdir -p "$PWD/mnt"
fi
if ! test -e "$PWD/mnt/$CAMERA"
then
mkdir -p "$PWD/mnt/$CAMERA"
fi
if ! test -e "$PWD/sqsh"
then
mkdir -p "$PWD/sqsh"
fi
if ! test -e "$PWD/images"
then
mkdir -p "$PWD/images"
fi

DOWNLOAD_TO="${PWD}/sqsh"

#Only download if it isn't already on my computer
if test -e "${DOWNLOAD_TO}/$CAMERA.sqsh"
then
    echo "$CAMERA.sqsh is already on local device"
else
    #Getting the credentials required to download from cadem
    read -p "CADEM account: " USERNAME
    DOWNLOAD_TO="${PWD}/sqsh"
    DOWNLOAD_FROM="$USERNAME@ssh.et.byu.edu:/fsc/$USERNAME/groups/aq-images/images/$CAMERA.sqsh"

    #The actual download happens here
    echo "Downloading $CAMERA"
    scp $DOWNLOAD_FROM $DOWNLOAD_TO
fi




#TODO: only mount if something else isn't mounted

#mounting the sqsh file
echo "Mounting $CAMERA"
mount -o loop "$DOWNLOAD_TO/$CAMERA.sqsh" "$PWD/mnt/$CAMERA"

#Finding and choosing the files to download
echo "\nYears avalible:"
ls "$PWD/mnt/$CAMERA"
read -p "Year: " YEAR

echo "\nMonths avalible:"
ls "$PWD/mnt/$CAMERA/$YEAR"
read -p "Month: " MONTH

# echo "\nDays avalible:"
# ls "$PWD/mnt/$CAMERA/$YEAR/$MONTH"
# read -p "Day: " DAY

#Clearning up the image folder so that it doesn't get crouded upon multiple itterations
rm -r "$PWD/images"
mkdir -p "$PWD/images/$YEAR/$MONTH"

#need to add back /DAY from above and below

#Copying the files over and making sure they have the correct permisions so that we can view them
cp -a "$PWD/mnt/$CAMERA/$YEAR/$MONTH/." "$PWD/images/$YEAR/$MONTH/"
echo "Printed"
chown -R kyle2004:kyle2004 "$PWD/images/"
chmod -R 664 "$PWD/images/$YEAR/$MONTH/"*
echo "permissions"


#Unmounting and cleaning up mnt
umount "$PWD/mnt/$CAMERA"
rmdir "$PWD/mnt/$CAMERA"

find "$PWD/images/$YEAR/$MONTH/" -type f -print0 | xargs -0 mv -t "$PWD/images/$YEAR/$MONTH"  
rmdir "$PWD/images/$YEAR/$MONTH/01"
rmdir "$PWD/images/$YEAR/$MONTH/02"
rmdir "$PWD/images/$YEAR/$MONTH/03"
rmdir "$PWD/images/$YEAR/$MONTH/04"
rmdir "$PWD/images/$YEAR/$MONTH/05"
rmdir "$PWD/images/$YEAR/$MONTH/06"
rmdir "$PWD/images/$YEAR/$MONTH/07"
rmdir "$PWD/images/$YEAR/$MONTH/08"
rmdir "$PWD/images/$YEAR/$MONTH/09"
rmdir "$PWD/images/$YEAR/$MONTH/10"
rmdir "$PWD/images/$YEAR/$MONTH/11"
rmdir "$PWD/images/$YEAR/$MONTH/12"
rmdir "$PWD/images/$YEAR/$MONTH/13"
rmdir "$PWD/images/$YEAR/$MONTH/14"
rmdir "$PWD/images/$YEAR/$MONTH/15"
rmdir "$PWD/images/$YEAR/$MONTH/16"
rmdir "$PWD/images/$YEAR/$MONTH/17"
rmdir "$PWD/images/$YEAR/$MONTH/18"
rmdir "$PWD/images/$YEAR/$MONTH/19"
rmdir "$PWD/images/$YEAR/$MONTH/20"
rmdir "$PWD/images/$YEAR/$MONTH/21"
rmdir "$PWD/images/$YEAR/$MONTH/22"
rmdir "$PWD/images/$YEAR/$MONTH/23"
rmdir "$PWD/images/$YEAR/$MONTH/24"
rmdir "$PWD/images/$YEAR/$MONTH/25"
rmdir "$PWD/images/$YEAR/$MONTH/26"
rmdir "$PWD/images/$YEAR/$MONTH/27"
rmdir "$PWD/images/$YEAR/$MONTH/28"
echo "moved"