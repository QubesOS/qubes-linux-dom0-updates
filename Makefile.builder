PACKAGES_FROM_FC28 := \
    device-mapper-persistent-data-0.7.5-3.fc28.src.rpm \
    xorg-x11-drv-nouveau-1.0.15-4.fc28.src.rpm \
    xorg-x11-drv-ati-18.0.1-1.fc28.src.rpm

# rebuild with updated rpm
PACKAGES_FROM_FC25 := \
  deltarpm-3.6-17.fc25.src.rpm \
  drpm-0.3.0-3.fc25.src.rpm \
  libsolv-0.6.29-2.fc25.src.rpm \
  createrepo_c-0.10.0-6.fc25.src.rpm \
  hawkey-0.6.4-3.fc25.src.rpm \
  satyr-0.21-2.fc25.src.rpm \
  PackageKit-1.1.5-1.fc25.src.rpm \
  grub2-2.02-0.38.fc25.src.rpm \
  systemtap-3.2-2.fc25.src.rpm \

# rebuild with Fedora 25 rpm, but with local patches
# HACK: When we pass the list of rpms to the Qubes build script, we
# append a "need-patch" suffix. Instructions for applying the patch
# is written in the Makefile in a case-by-case basis.
PACKAGES_FROM_FC25_NEED_PATCH := \
  xorg-x11-server-1.19.3-1.fc25.src.rpm

xorg-x11-server-1.19.3-1.need-patch.fc25.src.rpm:
	mkdir xorg-x11-server-1.19.3-1.need-patch.fc25.src.rpm
	rpm2cpio xorg-x11-server-1.19.3-1.fc25.src.rpm | cpio -ivd -D xorg-x11-server-1.19.3-1.need-patch.fc25.src.rpm
	patch -d xorg-x11-server-1.19.3-1.need-patch.fc25.src.rpm -p1 < xorg-x11-server-1.19.3-1-fix-vga-arbitration-overflow.patch

# used by Makefile, not relevant for RPM_SRC_PACKAGES
PACKAGES_FROM_FC25_UPDATES := \
  libsolv-0.6.29-2.fc25.src.rpm \
  hawkey-0.6.4-3.fc25.src.rpm \
  PackageKit-1.1.5-1.fc25.src.rpm \
  grub2-2.02-0.38.fc25.src.rpm \
  systemtap-3.2-2.fc25.src.rpm \
  xorg-x11-server-1.19.3-1.fc25.src.rpm

ifeq ($(DIST), fc25)
    RPM_SRC_PACKAGES.dom0 := $(PACKAGES_FROM_FC28:%.fc28.src.rpm=%.$(DIST).src.rpm) \
                             $(PACKAGES_FROM_FC25)
    RPM_SOURCE_DIR := $(DIST_SRC_ROOT)/$(COMPONENT)/xorg-x11-server-1.19.3-1.need-patch.fc25.src.rpm/
    RPM_SPEC_FILES := xorg-x11-server-1.19.3-1.need-patch.fc25.src.rpm/xorg-x11-server.spec
endif

# Increase versions to force the update of rebuilt packages.
RPM_BUILD_EXTRA_DEFINES += --define="dist .1.fc25"


RPM_SRC_PACKAGES := $(RPM_SRC_PACKAGES.$(PACKAGE_SET))
