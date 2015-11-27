ifeq ($(PACKAGE_SET),dom0)
    RPM_SRC_PACKAGES := \
						wayland-1.6.0-1.fc21.src.rpm \
						xorg-x11-server-1.16.3-2.fc21.src.rpm \
    					xorg-x11-drv-ati-7.5.0-1.fc21.src.rpm \
    					xorg-x11-drv-dummy-0.3.6-20.fc21.src.rpm \
    					xorg-x11-drv-evdev-2.9.1-2.fc21.src.rpm \
    					xorg-x11-drv-fbdev-0.4.3-19.fc21.src.rpm \
    					xorg-x11-drv-fbturbo-0.5.1-0.2.20150221.fc21.src.rpm \
    					xorg-x11-drv-intel-2.99.916-4.20141117.fc21.src.rpm \
    					xorg-x11-drv-ivtv-1.2.0-0.15.fc21.src.rpm \
    					xorg-x11-drv-modesetting-0.9.0-2.fc21.src.rpm \
    					xorg-x11-drv-nouveau-1.0.11-1.fc21.src.rpm \
    					xorg-x11-drv-openchrome-0.3.3-12.fc21.src.rpm \
    					xorg-x11-drv-qxl-0.1.2-1.fc21.src.rpm \
    					xorg-x11-drv-sisusb-0.9.6-18.fc21.src.rpm \
    					xorg-x11-drv-synaptics-1.8.1-6.fc21.src.rpm \
    					xorg-x11-drv-v4l-0.2.0-41.fc21.src.rpm \
    					xorg-x11-drv-vesa-2.3.2-19.fc21.src.rpm \
    					xorg-x11-drv-vmmouse-13.0.0-13.fc21.src.rpm \
    					xorg-x11-drv-vmware-13.0.2-8.20150211git8f0cf7c.fc21.src.rpm \
    					xorg-x11-drv-void-1.4.0-27.fc21.src.rpm \
    					xorg-x11-drv-voodoo-1.2.5-18.fc21.src.rpm \
    					xorg-x11-drv-wacom-0.25.0-2.fc21.src.rpm

    RPM_SPEC_FILES := xorg-x11-drivers.spec build-deps-qxl.spec
endif

# vim: ft=make
