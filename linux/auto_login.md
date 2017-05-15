Haven't tried this on a PI but this is what I do on another ARM based SBC....

Only works if you are running lightdm...

Edit:

/usr/share/lightdm/lightdm.conf.d/60-lightdm-gtk-greeter.conf

Then add the following line at the end:

autologin-user=pi


Bruce
