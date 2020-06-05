PACKAGES_FROM_FC28 := \
  rpm-4.14.2.1-2.fc28.src.rpm \
  python-systemd-234-5.fc28.src.rpm
PACKAGES_FROM_FC28_UPDATES := \
  rpm-4.14.2.1-2.fc28.src.rpm
# rebuild with updated rpm
PACKAGES_FROM_FC25 := \
  deltarpm-3.6-17.fc25.src.rpm \
  drpm-0.3.0-3.fc25.src.rpm \
  libsolv-0.6.29-2.fc25.src.rpm \
  createrepo_c-0.10.0-6.fc25.src.rpm \
  hawkey-0.6.4-3.fc25.src.rpm \
  satyr-0.21-2.fc25.src.rpm \
  PackageKit-1.1.5-1.fc25.src.rpm \
  grub2-2.02-0.38.fc25.src.rpm

# used by Makefile, not relevant for RPM_SRC_PACKAGES
PACKAGES_FROM_FC25_UPDATES := \
  libsolv-0.6.29-2.fc25.src.rpm \
  hawkey-0.6.4-3.fc25.src.rpm \
  PackageKit-1.1.5-1.fc25.src.rpm \
  grub2-2.02-0.38.fc25.src.rpm

ifeq ($(DIST), fc25)
    RPM_SRC_PACKAGES.dom0 := $(PACKAGES_FROM_FC28:%.fc28.src.rpm=%.$(DIST).src.rpm) \
                             $(PACKAGES_FROM_FC25)
endif

# Avoid libimaevm dep on rpm, and also increase versions to force the update.
# Define _without_libimaevm directly instead of --without=libimaevm, to have
# dnf builddep understand it too.
RPM_BUILD_EXTRA_DEFINES += --define="_without_libimaevm 1" --define="dist .1.fc25" --nocheck

RPM_SRC_PACKAGES := $(RPM_SRC_PACKAGES.$(PACKAGE_SET))
