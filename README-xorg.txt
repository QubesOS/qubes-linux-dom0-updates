Xorg drivers packages preparation.

The procedure is already done in this repository, placed here just for
reference and for future updates.

1. Remove old packages:
   rm -f xorg-x11-drv-*src.rpm
2. Download packages:
   yumdownloader --releasever=17 --disablerepo=* --enablerepo=fedora,updates --source 'xorg-x11-drv-*'
3. Remove not needed/not compatible one:
    # does not support x86_64
    rm -f xorg-x11-drv-geode-*src.rpm
    rm -f xorg-x11-drv-neomagic-*src.rpm
    # not used in Qubes
    rm -f xorg-x11-drv-qxl-*src.rpm
    rm -f xorg-x11-drv-vmware-*src.rpm
    # anyone using this acient hardware?
    rm -f xorg-x11-drv-r128-*src.rpm
    rm -f xorg-x11-drv-s3-*src.rpm
    rm -f xorg-x11-drv-s3virge-*src.rpm
    rm -f xorg-x11-drv-s3virge-*src.rpm
4. Verify downloaded packages
   rpm -K *.src.rpm | grep -v 'pgp md5 OK$$'
  Above command will list INVALID packages. If any is listed, stop here and
  investigate why, perhaps redownload it.
  You should have Fedora-17 gpg key imported (rpm --import <path-to-key>).

5. Fix some packages:
 (replace "file" with package name)
 rpm -i file*.src.rpm
 edit ~/rpmbuild/SPECS/file.spec
  add "--force" option to "autoreconf" command in %build section
 rebuild source rpm:
 rpmbuild -bs ~/rpmbuild/SPECS/file.spec
 replace original file*src.rpm with one from ~/rpmbuild/SRPMS

 Repeat above procedure for:
 xorg-x11-drv-evdev-*.src.rpm
 xorg-x11-drv-mouse-*.src.rpm
 xorg-x11-drv-keyboard-*.src.rpm
 xorg-x11-drv-void-*.src.rpm
