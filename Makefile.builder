PACKAGES_FROM_FC28 := \
    device-mapper-persistent-data-0.7.5-3.fc28.src.rpm \
    xorg-x11-drv-nouveau-1.0.15-4.fc28.src.rpm \
    xorg-x11-drv-ati-18.0.1-1.fc28.src.rpm

ifeq ($(shell expr $(subst fc,,$(DIST)) \<= 27 2>/dev/null),1)
    RPM_SRC_PACKAGES.dom0 := $(PACKAGES_FROM_FC28:%.fc28.src.rpm=%.$(DIST).src.rpm)
endif

RPM_SRC_PACKAGES := $(RPM_SRC_PACKAGES.$(PACKAGE_SET))
