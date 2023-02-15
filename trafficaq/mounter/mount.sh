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

echo "\nDays avalible:"
ls "$PWD/mnt/$CAMERA/$YEAR/$MONTH"
read -p "Day: " DAY

#Clearning up the image folder so that it doesn't get crouded upon multiple itterations
rm -r "$PWD/images"
mkdir -p "$PWD/images/$YEAR/$MONTH/$DAY"

#Copying the files over and making sure they have the correct permisions so that we can view them
cp -av "$PWD/mnt/$CAMERA/$YEAR/$MONTH/$DAY/." "$PWD/images/$YEAR/$MONTH/$DAY/"
chown -R kyle2004:kyle2004 "$PWD/images/"
chmod 660 "$PWD/images/$YEAR/$MONTH/$DAY/"*


#Unmounting and cleaning up mnt
umount "$PWD/mnt/$CAMERA"
rmdir "$PWD/mnt/$CAMERA"