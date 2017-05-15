In the file you put in /etc/init.d/ you have to set it executable with:

    chmod +x /etc/init.d/start_my_app
Thanks to @meetamit, if this does not run you have to create a symlink to /etc/rc.d/

    ln -s /etc/init.d/start_my_app /etc/rc.d/
Please note that on latest Debian, this will not work as your script have to be LSB compliant (provide, at least, the following actions: start, stop, restart, force-reload, and status): https://wiki.debian.org/LSBInitScripts

As a note, you should put the absolute path of your script instead of a relative one, it may solves unexpected issues:

    /var/myscripts/start_my_app
And don't forget to add on top of that file:

    #!/bin/sh
