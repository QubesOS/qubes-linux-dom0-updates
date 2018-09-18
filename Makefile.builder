XORG_DRIVERS_FROM_FC28 := \
    xorg-x11-drv-intel-2.99.917-32.20171025.fc28.src.rpm \
    xorg-x11-drv-ati-18.0.1-1.fc28.src.rpm

ifeq ($(shell expr $(subst fc,,$(DIST)) \<= 27 2>/dev/null),1)
    RPM_SRC_PACKAGES.dom0 := $(XORG_DRIVERS_FROM_FC28)
endif

RPM_SRC_PACKAGES := $(RPM_SRC_PACKAGES.$(PACKAGE_SET))
