sudo apt-get install --install-recommends linux-generic-lts-xenial xserver-xorg-core-lts-xenial xserver-xorg-lts-xenial xserver-xorg-video-all-lts-xenial xserver-xorg-input-all-lts-xenial libwayland-egl1-mesa-lts-xenial

sudo apt-get install linux-image-generic-lts-xenial

sudo apt-get install libusb-1.0-0-dev pkg-config

For Ubuntu 14.04: use * ./scripts/install_glfw3.sh

For Ubuntu 16.04 install glfw3 via * sudo apt-get install libglfw3-dev

sudo reboot

if error: sudo apt-get --reinstall install 'ros-*-librealsense'
