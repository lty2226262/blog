I own a bunch of devices that appear as /dev/ttyUSB<something> in the system. At least three of them I use regularly: Arduino, BusPirate and a simple USB-to-RS232 converter to talk to my ARM boards. I keep plugging them in and pulling them out from the USB ports and they keep getting names like /dev/ttyUSB0 or ttyUSB1 or ttyUSB2 or so. Sadly the device names are not persistent — whether the BusPirate pops up as /dev/ttyUSB0 or /dev/ttyUSB2 depends on the order in which are the devices discovered by the kernel. That makes things difficult — it usually requires a trial and error approach to find out what the hell is the ARM board’s tty name this time.

Wouldn’t it be nice to have persistent, descriptive device name for each of these toys? Like /dev/arduino, /dev/buspirate and /dev/arm?

## usb-serial devices

All the above mentioned gadgets have usb-serial interface, which in essence means that the serial port traffic (UART) is passed to the host in a USB data stream instead of through a dedicated RS232 serial port.

Every USB device has a Vendor ID and a Product ID as seen for instance in lsusb output:

    ~ # lsusb
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 011: ID 0403:6001 FTDI FT232 USB-Serial (UART) IC
    Bus 001 Device 010: ID 0403:6001 FTDI FT232 USB-Serial (UART) IC
    Bus 001 Device 005: ID 0402:5632 ALi Corp. USB 2.0 Host-to-Host Link
    Bus 002 Device 005: ID 0403:6001 FTDI FT232 USB-Serial (UART) IC
    [...]
Unfortunately all the three peripherals apparently use the same chip — FT232 (these days probably the most common usb-serial interface) and therefore have the same VendorID:ProductID pair as emphasized in the listing. To distinguish between them we need some other unique identifier — in this case a serial number. These are the messages recorded in /var/log/messages when Arduino is plugged in:

    usb 2-4: new full speed USB device using ohci_hcd and address 5
    ftdi_sio 2-4:1.0: FTDI USB Serial Device converter detected
    drivers/usb/serial/ftdi_sio.c: Detected FT232RL
    usb 2-4: FTDI USB Serial Device converter now attached to ttyUSB1
    usb 2-4: New USB device found, idVendor=0403, idProduct=6001
    usb 2-4: Product: FT232R USB UART
    usb 2-4: Manufacturer: FTDI
    usb 2-4: SerialNumber: A6008isP
(Update, as pointed out by Martijn in the comments…) Another way to find out the serial number is using udevadm command:

    ~ # udevadm info -a -n /dev/ttyUSB1 | grep '{serial}' | head -n1
        ATTRS{serial}=="A6008isP"
## UDEV rules

Now with the list of serial numbers in hand let’s create a UDEV ruleset that’ll make a nice symbolic link for each of these devices. UDEV rules are usually scattered into many files in /etc/udev/rules.d. Create a new file called 99-usb-serial.rules and put the following lines in there:

    SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="A6008isP", SYMLINK+="arduino", MODE="0777"
    SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="A7004IXj", SYMLINK+="buspirate"
    SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", ATTRS{serial}=="FTDIF46B", SYMLINK+="ttyUSB.ARM"
By now it should be obvious what these lines mean. Perhaps just a note for the last entry on each line — SYMLINK+="arduino" means that UDEV should create a symlink /dev/arduino pointing to the actual /dev/ttyUSB* device. In other words the device names will continue to be assigned ad-hoc but the symbolic links will always point to the right device node. Let’s see. Unplug Arduino and plug it back again…

    ~# ls -l /dev/arduino
    lrwxrwxrwx 1 root root 7 Nov 25 22:12 /dev/arduino -> ttyUSB1

    ~# ls -l /dev/ttyUSB1
    crw-rw---- 1 root uucp 188, 0 Nov 25 22:12 /dev/ttyUSB1
That looks good. The last step is to configure minicom, avrdude and all the other relevant tools to use these new names and forget about chasing the right /dev/ttyUSB* every second day.
