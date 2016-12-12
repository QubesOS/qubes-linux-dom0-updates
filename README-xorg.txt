Xorg drivers packages preparation.

The procedure is already done in this repository, placed here just for
reference and for future updates.

1. Remove old packages:
   rm -f xorg-x11-drv-*src.rpm
2. Download packages:
   yumdownloader --releasever=21 --disablerepo=* --enablerepo=fedora,updates --source 'xorg-x11-drv-*' 'xorg-x11-server' 'wayland'
3. Remove not needed/not compatible one:
    # does not support x86_64
    rm -f xorg-x11-drv-armsoc-*.src.rpm
    rm -f xorg-x11-drv-freedreno-*.src.rpm
    rm -f xorg-x11-drv-omap-*src.rpm
    rm -f xorg-x11-drv-opentegra-*src.rpm
    # not used in Qubes
    rm -f xorg-x11-drv-qxl-*src.rpm
4. Verify downloaded packages
   rpm -K *.src.rpm | grep -v 'pgp md5 OK$'
  Above command will list INVALID packages. If any is listed, stop here and
  investigate why, perhaps redownload it.
  You should have Fedora-21 gpg key imported (rpm --import <path-to-key>).
