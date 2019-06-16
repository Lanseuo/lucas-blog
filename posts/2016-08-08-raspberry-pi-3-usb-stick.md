---
title: Raspberry Pi 3 vom USB-Stick booten
image: DSC_0004.JPG
description: In dieser Anleitung erfährst du Schritt-für-Schritt, wie Du an einem Raspberry Pi 3 von einem USB-Stick oder von einer Fesplatte booten kannst.
---

Vor ein paar Tagen hat die [Raspberry Pi Foundation](https://www.raspberrypi.org/blog/pi-3-booting-part-i-usb-mass-storage-boot/) angekündigt, dass man mit der neuen Beta auch von einem USB-Stick oder einer Festplatte booten kann. Ich finde das sehr praktisch, da man so nicht immer das Gehäuse auseinander schrauben muss, nur um die SD-Karte auszutauschen, wenn man mal ein anderes Betriebssystem ausprobieren will. Diese Funktion ist aber nur für den neuen [Raspberry Pi 3*](https://amzn.to/2Xf0MyJ) verfügbar und es werden außerdem auch noch nicht alle USB-Sticks unterstützt.

# Unterstützte USB-Sticks

Laut Gordon Hollingworth funktioniert dieser Vorgang mit folgenden USB-Sticks:

- Sandisk Cruzer Fit 16GB
- Sandisk Cruzer Blade 16Gb
- Samsung 32GB USB 3.0 drive
- MeCo 16GB USB 3.0

# USB Boot aktivieren

Als erstes brauchst Du ein normales Raspian Image. Dieses lädst Du dir von der [offiziellen Raspberry Pi Download Seite](https://www.raspberrypi.org/downloads/) herunter und schreibst es auf deine micro-SD-Karte. Zu beginn machst Du ein Update von Raspian.

    sudo apt-get update -y && sudo apt-get upgrade

Da diese Funktion derzeit nur in der Beta von Raspian verfügbar ist, muss diese installiert werden und anschließend der Raspberry Pi neu gestartet werden.

    sudo BRANCH=next rpi-update
    sudo reboot

Nun aktivierst Du den USB Boot Mode in der config.txt und startest den Pi nocheinmal neu.

    echo program_usb_boot_mode=1 | sudo tee -a /boot/config.txt
    sudo reboot

Das hat die Zeile echo program\_usb\_boot_mode=1 an das Ende der conig.txt-Datei gesetzt. Um zu überprüfen, ob der Vorgang geklappt hat, gibst Du folgenden Befehl ein.

    vcgencmd otp_dump | grep 17:

Hierbei solltest du die Ausgabe **17:3020000a** bekommen. Falls das nicht der Fall ist, hat etwas nicht geklappt.

# Den USB-Stick vorbereiten

Als nächstes muss der USB-Stick vorbereitet werden. Dafür steckst Du ihn als erstes in den Raspberry Pi ein. Mit Parted erstellst Du eine 100MB fat32 Partition und eine Linux ext4 Partition.

    sudo parted /dev/sda

In Parted startest Du msdos.

    (parted) mktable msdos

Dies bestätigst Du mit **Yes**.

    (parted) mkpart primary fat32 0% 100M
    (parted) mkpart primary ext4 100M 100%


Nun erstellst du ein boot und ein root Dateisystem.

    sudo mkfs.vfat -n BOOT -F 32 /dev/sda1
    sudo mkfs.ext4 /dev/sda2

Das Dateisystem wird eingebunden und Raspian wird auf den Stick kopiert.

    sudo mkdir /mnt/target
    sudo mount /dev/sda2 /mnt/target/
    sudo mkdir /mnt/target/boot
    sudo mount /dev/sda1 /mnt/target/boot/
    sudo apt-get update; sudo apt-get install rsync
    sudo rsync -ax --progress / /boot /mnt/target

Als nächsten Schritt richtest Du SSH ein.

    cd /mnt/target
    sudo mount --bind /dev dev
    sudo mount --bind /sys sys
    sudo mount --bind /proc proc
    sudo chroot /mnt/target
    rm /etc/ssh/ssh_host*
    dpkg-reconfigure openssh-server
    exit
    sudo umount dev
    sudo umount sys
    sudo umount proc

Nun veränderst Du /boot/cmdline.txt, so dass es den USB-Stick anstelle von der SD-Karte zum booten verwendet.

    sudo sed -i "s,root=/dev/mmcblk0p2,root=/dev/sda2," /mnt/target/boot/cmdline.txt

Dasselbe muss für fstab getan werden.

    sudo sed -i "s,/dev/mmcblk0p,/dev/sda," /mnt/target/etc/fstab

Nun wird der USB-Stick noch ausgeworfen und der Raspberry Pi wird neu gestartet.

    cd ~
    sudo umount /mnt/target/boot
    sudo umount /mnt/target
    sudo poweroff

Als letzten Schritt nimmst Du den Pi vom Strom, entfernst die SD-Karte und steckst das Netzteil wieder ein. Nun sollte der [Raspberry Pi*](https://amzn.to/2IkDpvu) von der SD-Karte starten. Dieser Vorgang dauert etwas länger, als der normale Start von der SD-Karte.
