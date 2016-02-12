%global checkout 91d5dd13
%global firmware_release 61

%global _firmwarepath	/usr/lib/firmware

Name:		linux-firmware
Version:	20160204
Release:	%{firmware_release}.git%{checkout}%{?dist}
Summary:	Firmware files used by the Linux kernel

Group:		System Environment/Kernel
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL:		http://www.kernel.org/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Provides:	kernel-firmware = %{version} xorg-x11-drv-ati-firmware = 7.0
Obsoletes:	kernel-firmware < %{version} xorg-x11-drv-ati-firmware < 6.13.0-0.22
Obsoletes:	ueagle-atm4-firmware < 1.0-5
Obsoletes:	netxen-firmware < 4.0.534-9
Obsoletes:	ql2100-firmware < 1.19.38-8
Obsoletes:	ql2200-firmware < 2.02.08-8
Obsoletes:	ql23xx-firmware < 3.03.28-6
Obsoletes:	ql2400-firmware < 5.08.00-2
Obsoletes:	ql2500-firmware < 5.08.00-2
Obsoletes:	rt61pci-firmware < 1.2-11
Obsoletes:	rt73usb-firmware < 1.8-11
Obsoletes:	cx18-firmware < 20080628-10
Obsoletes:	ivtv-firmware
Conflicts:	microcode_ctl < 2.1-0

BuildRequires: git

%description
This package includes firmware files required for some devices to
operate.

%package -n iwl100-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 100 Series Adapters
License:	Redistributable, no modification permitted
Version:	39.31.5.1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl100-firmware < 39.31.5.1-4
%description -n iwl100-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl100 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl105-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 105 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
%description -n iwl105-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl105 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl135-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 135 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
%description -n iwl135-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl135 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl1000-firmware
Summary:	Firmware for Intel® PRO/Wireless 1000 B/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	39.31.5.1
Epoch:		1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl1000-firmware < 1:39.31.5.1-3
%description -n iwl1000-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl1000 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl2000-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2000 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
%description -n iwl2000-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl2000 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl2030-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2030 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
%description -n iwl2030-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux to support the iwl2030 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl3945-firmware
Summary:	Firmware for Intel® PRO/Wireless 3945 A/B/G network adaptors
License:	Redistributable, no modification permitted
Version:	15.32.2.9
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl3945-firmware < 15.32.2.9-7
%description -n iwl3945-firmware
This package contains the firmware required by the iwl3945 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl4965-firmware
Summary:	Firmware for Intel® PRO/Wireless 4965 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	228.61.2.24
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl4965-firmware < 228.61.2.24-5
%description -n iwl4965-firmware
This package contains the firmware required by the iwl4965 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5000-firmware
Summary:	Firmware for Intel® PRO/Wireless 5000 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	8.83.5.1_1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl5000-firmware < 8.83.5.1_1-3
%description -n iwl5000-firmware
This package contains the firmware required by the iwl5000 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5150-firmware
Summary:	Firmware for Intel® PRO/Wireless 5150 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	8.24.2.2
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl5150-firmware < 8.24.2.2-4
%description -n iwl5150-firmware
This package contains the firmware required by the iwl5150 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6000 AGN Adapter
License:	Redistributable, no modification permitted
Version:	9.221.4.1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl6000-firmware < 9.221.4.1-4
%description -n iwl6000-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000g2a-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6005 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl6000g2a-firmware < 17.168.5.3-3
%description -n iwl6000g2a-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000g2b-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6030 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl6000g2b-firmware < 17.168.5.2-3
%description -n iwl6000g2b-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6050-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6050 Series Adapters
License:	Redistributable, no modification permitted
Version:	41.28.5.1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl6050-firmware < 41.28.5.1-5
%description -n iwl6050-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl7260-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 7260 Series Adapters
License:	Redistributable, no modification permitted
Epoch:		1
Version:	25.30.13.0
Release:	%{firmware_release}%{?dist}
%description -n iwl7260-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl3160-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 3160 Series Adapters
License:	Redistributable, no modification permitted
Epoch:		1
Version:	25.30.13.0
Release:	%{firmware_release}%{?dist}
%description -n iwl3160-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n libertas-usb8388-firmware
Summary:	Firmware for Marvell Libertas USB 8388 Network Adapter
License:	Redistributable, no modification permitted
Epoch:		2 
Obsoletes:	libertas-usb8388-firmware < 2:5.110.22.p23-8
%description -n libertas-usb8388-firmware
Firmware for Marvell Libertas USB 8388 Network Adapter

%package -n libertas-usb8388-olpc-firmware
Summary:	OLPC firmware for Marvell Libertas USB 8388 Network Adapter
License:	Redistributable, no modification permitted
%description -n libertas-usb8388-olpc-firmware
Firmware for Marvell Libertas USB 8388 Network Adapter with OLPC mesh network
support.

%package -n libertas-sd8686-firmware
Summary:	Firmware for Marvell Libertas SD 8686 Network Adapter
License:	Redistributable, no modification permitted
Obsoletes:	libertas-sd8686-firmware < 9.70.20.p0-4
%description -n libertas-sd8686-firmware
Firmware for Marvell Libertas SD 8686 Network Adapter

%package -n libertas-sd8787-firmware
Summary:	Firmware for Marvell Libertas SD 8787 Network Adapter
License:	Redistributable, no modification permitted
%description -n libertas-sd8787-firmware
Firmware for Marvell Libertas SD 8787 Network Adapter

%prep
%setup -q -n linux-firmware-%{checkout}
%if 0
git init .
if [ -z "$GIT_COMMITTER_NAME" ]; then
    git config user.email "nobody@fedoraproject.org"
    git config user.name "Fedora linux-firmware packagers"
fi
git add .
git commit -m init .

%endif

%build
# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
rm -rf ess korg sb16 yamaha

# Remove source files we don't need to install
rm -f usbdux/*dux */*.asm
rm -rf carl9170fw

# No need to install old firmware versions where we also provide newer versions
# which are preferred and support the same (or more) hardware
rm -f libertas/sd8686_v8*
rm -f libertas/usb8388_v5.bin

# Remove firmware for Creative CA0132 HD as it's in alsa-firmware
rm -f ctefx.bin ctspeq.bin

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_firmwarepath}
mkdir -p $RPM_BUILD_ROOT/%{_firmwarepath}/updates
cp -r * $RPM_BUILD_ROOT/%{_firmwarepath}
rm $RPM_BUILD_ROOT/%{_firmwarepath}/{WHENCE,LICENCE.*,LICENSE.*}

# Create file list but exclude firmwares that we place in subpackages
FILEDIR=`pwd`
pushd $RPM_BUILD_ROOT/%{_firmwarepath}
find . \! -type d > $FILEDIR/linux-firmware.files
find . -type d | sed -e '/^.$/d' > $FILEDIR/linux-firmware.dirs
popd
sed -i -e 's:^./::' linux-firmware.{files,dirs}
sed -i -e '/^iwlwifi/d' \
	-i -e '/^libertas\/sd8686/d' \
	-i -e '/^libertas\/usb8388/d' \
	-i -e '/^mrvl\/sd8787/d' \
	linux-firmware.files
sed -i -e 's!^!/usr/lib/firmware/!' linux-firmware.{files,dirs}
sed -e 's/^/%%dir /' linux-firmware.dirs >> linux-firmware.files

%clean
rm -rf $RPM_BUILD_ROOT

%files -n iwl100-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-100-5.ucode

%files -n iwl105-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-105-*.ucode

%files -n iwl135-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-135-*.ucode

%files -n iwl1000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-1000-*.ucode

%files -n iwl2000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-2000-*.ucode

%files -n iwl2030-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-2030-*.ucode

%files -n iwl3945-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3945-*.ucode

%files -n iwl4965-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-4965-*.ucode

%files -n iwl5000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-5000-*.ucode

%files -n iwl5150-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-5150-*.ucode

%files -n iwl6000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6000-*.ucode

%files -n iwl6000g2a-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6000g2a-*.ucode

%files -n iwl6000g2b-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6000g2b-*.ucode

%files -n iwl6050-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-6050-*.ucode

%files -n iwl7260-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-7260-*.ucode
%{_firmwarepath}/iwlwifi-7265-*.ucode
%{_firmwarepath}/iwlwifi-7265D-*.ucode
%{_firmwarepath}/iwlwifi-8000C-*.ucode

%files -n iwl3160-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{_firmwarepath}/iwlwifi-3160-*.ucode

%files -n libertas-usb8388-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.Marvell
%dir %{_firmwarepath}/libertas
%{_firmwarepath}/libertas/usb8388_v9.bin

%files -n libertas-usb8388-olpc-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.Marvell
%dir %{_firmwarepath}/libertas
%{_firmwarepath}/libertas/usb8388_olpc.bin

%files -n libertas-sd8686-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.Marvell
%dir %{_firmwarepath}/libertas
%{_firmwarepath}/libertas/sd8686*

%files -n libertas-sd8787-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.Marvell
%dir %{_firmwarepath}/mrvl
%{_firmwarepath}/mrvl/sd8787*

%files -f linux-firmware.files
%defattr(-,root,root,-)
%dir %{_firmwarepath}
%doc WHENCE LICENCE.* LICENSE.*

%changelog
* Thu Feb 04 2016 Josh Boyer <jwboyer@fedoraproject.org> 20160204-61.git91d5dd13
- Update to latest upstream snashot
- rtlwifi, iwlwifi, intel bluetooth, skylake audio updates

* Mon Dec 14 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151214-60.gitbbe4917c
- Update to latest upstream snapshot
- Includes firmware for mt7601u (rhbz 1264631)

* Mon Nov 30 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151130-59.gita109a8ff
- Update to latest upstream snapshot
- Includes -16 ucode for iwlwifi, skylake dmc and audio updates, brcm updates
  bnx2x, and others

* Fri Oct 30 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151030-58.git66d3d8d7
- Update to latest upstream snapshot
- Includes ath10k and mwlwifi firmware updates (rhbz 1276360)

* Mon Oct 12 2015 Josh Boyer <jwboyer@fedoraproject.org> 20151012-57.gitd82d3c1e
- Update to latest upstream snapshot
- Includes skylake and intel bluetooth firmware updates

* Fri Sep 04 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150904-56.git6ebf5d57
- Update to latest upstream git snapshot
- Includes amdgpu firmware and skylake updates

* Thu Sep 03 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150903-55.git38358cfc
- Add firmware from Alex Deucher for amdgpu driver (rhbz 1259542)

* Thu Sep 03 2015 Josh Boyer <jwboyer@fedoraproject.org>
- Update to latest upstream git snapshot
- Updates for nvidia, bnx2x, and atmel devices

* Wed Jul 15 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150715-54.git69640304
- Update to latest upstream git snapshot
- New iwlwifi firmware for 726x/316x/8000 devices
- New firmware for i915 skylake and radeon devices
- Various other updates

* Tue Jun 23 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150521-53.git3161bfa4
- Don't obsolete ivtv-firmware any longer (rhbz 1232773)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150521-52.git3161bfa4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150521-52.git3161bfa4
- Update to latest upstream git snapshot
- Updated iwlwifi 316x/726x firmware
- Add cx18-firmware Obsoletes from David Ward (rhbz 1222164)

* Wed May 06 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-51.gitec89525b
- Obsoletes ivtv-firmware (rbhz 1211055)

* Fri May 01 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-50.gitec89525b
- Add v4l-cx25840.fw back now that ivtv-firmware is retired (rhbz 1211055)

* Tue Apr 14 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-49.gitec89525b
- Fix conflict with ivtv-firmware (rhbz 1203385)

* Fri Apr 10 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150415-47.gitec89525b
- Update to the latest upstream git snapshot

* Thu Mar 19 2015 Josh Boyer <jwboyer@fedoraproject.org>
- Ship the cx18x firmware files (rhbz 1203385)

* Mon Mar 16 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150316-46.git020e534e
- Update to latest upstream git snapshot

* Fri Feb 13 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150213-45.git17657c35
- Update to latest upstream git snapshot
- Firmware for Surface Pro 3 WLAN/Bluetooth (rhbz 1185804)

* Thu Jan 15 2015 Josh Boyer <jwboyer@fedoraproject.org> 20150115-44.git78535e88.fc22
- Update to latest upstream git snapshot
- Adjust iwl{3160,7260} version numbers (rhbz 1167695)

* Tue Oct 14 2014 Josh Boyer <jwboyer@fedoraproject.org> 20141013-43.git0e5f6377.fc22
- Fix 3160/7260 version numbers (rhbz 1110522)

* Mon Oct 13 2014 Josh Boyer <jwboyer@fedoraproject.org> 20141013-42.git0e5f6377.fc22
- Update to latest upstream git snapshot

* Fri Sep 12 2014 Josh Boyer <jwboyer@fedoraproject.org> 20140912-41.git365e80cce.fc22
- Update to the latest upstream git snapshot

* Thu Aug 28 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Update to latest upstream git snapshot for new radeon firmware (rhbz 1130738)
- Fix versioning after mass rebuild and for iwl5000-firmware (rhbz 1130979)

* Fri Aug 08 2014 Kyle McMartin <kyle@fedoraproject.org> 20140808-39.gitce64fa89.1
- Update from upstream linux-firmware.
- Nuke unapplied radeon patches.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140605-38.gita4f3bc03.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Josh Boyer <jwboyer@fedoraproject.org> - 20140605-38.gita4f3bc03
- Updates for Intel 3160/7260/7265 firmware (1087717)
- Add firmware for rtl8723be (rhbz 1091753)
- Updates for radeon CIK, SI/CI, and Mullins/Beema GPUs (rhbz 1094153)
- Various other firmware updates

* Mon Mar 17 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Updates for Intel 3160/7260 and BCM43362 (rhbz 1071590)

* Tue Mar 04 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Fixup Intel wireless package descriptions and Source0 (rhbz 1070600)

* Fri Jan 31 2014 Josh Boyer <jwboyer@fedoraproject.org> - 20140131-35.gitd7f8a7c8
- Update to new snapshot
- Updates for Intel 3160/7260, radeon HAWAII GPUs, and some rtlwifi chips
- Fixes bugs 815579 1046935

* Tue Oct 01 2013 Kyle McMartin <kyle@fedoraproject.org> - 20131001-32.gitb8ac7c7e
- Update to a new git snapshot, drop radeon patches.

* Mon Sep 16 2013 Josh Boyer <jwboyer@fedoraproject.org> - 20130724-31.git31f6b30
- Obsolete ql2x00-firmware packages again (rhbz 864959)

* Sat Jul 27 2013 Josh Boyer <jwboyer@redhat.com> - 20130724-30.git31f6b30
- Add AMD ucode back in now that microcode_ctl doesn't provide it

* Fri Jul 26 2013 Dave Airlie <airlied@redhat.com> 20130724-29.git31f6b30
- add radeon firmware which are lost on the way upstream (#988268)

* Thu Jul 25 2013 Josh Boyer <jwboyer@redhat.com> - 20130724-28.git31f6b30
- Temporarily remove AMD microcode (rhbz 988263)
- Remove Creative CA0132 HD-audio files as they're in alsa-firmware

* Wed Jul 24 2013 Josh Boyer <jwboyer@redhat.com> - 20130724-27.git31f6b30
- Update to latest upstream
- New rtl, iwl, and amd firmware

* Fri Jun 07 2013 Josh Boyer <jwboyer@redhat.com> - 20130607-26.git2892af0
- Update to latest upstream release
- New radeon, bluetooth, rtl, and wl1xxx firmware

* Mon May 20 2013 Kyle McMartin <kyle@redhat.com> - 20130418-25.gitb584174
- Use a common version number for both the iwl*-firmware packages and
  linux-firmware itself.
- Don't reference old kernel-firmware package in %description

* Mon May 20 2013 Kyle McMartin <kyle@redhat.com> - 20130418-0.3.gitb584174
- Bump iwl* version numbers as well...

* Mon May 20 2013 Kyle McMartin <kyle@redhat.com> - 20130418-0.2.gitb584174
- UsrMove: move firmware to /usr/lib/firmware
- Remove duplicate /usr/lib/firmware/updates entry (already in linux-firmware.dirs)
- Simplify sed by using '!' instead of '/' as regexp delimiter
- Fix date error (commited on Mon Feb 04, so change that entry)

* Thu Apr 18 2013 Josh Boyer <jwboyer@redhat.com> - 20130418-0.1.gitb584174
- Update to latest upstream git tree

* Tue Mar 19 2013 Josh Boyer <jwboyer@redhat.com>
- Own the firmware directories (rhbz 919249)

* Thu Feb 21 2013 Josh Boyer <jwboyer@redhat.com> - 20130201-0.4.git65a5163
- Obsolete netxen-firmware.  Again.  (rhbz 913680)

* Mon Feb 04 2013 Josh Boyer <jwboyer@redhat.com> - 20130201-0.3.git65a5163
- Obsolete ql2[45]00-firmware packages (rhbz 906898)
 
* Fri Feb 01 2013 Josh Boyer <jwboyer@redhat.com> 
- Update to latest upstream release
- Provide firmware for carl9170 (rhbz 866051)

* Wed Jan 23 2013 Ville Skyttä <ville.skytta@iki.fi> - 20121218-0.2.gitbda53ca
- Own subdirs created in /lib/firmware (rhbz 902005)

* Wed Jan 23 2013 Josh Boyer <jwboyer@redhat.com>
- Correctly obsolete the libertas-usb8388-firmware packages (rhbz 902265)

* Tue Dec 18 2012 Josh Boyer <jwboyer@redhat.com>
- Update to latest upstream.  Adds brcm firmware updates

* Wed Oct 10 2012 Josh Boyer <jwboyer@redhat.com>
- Consolidate rt61pci-firmware and rt73usb-firmware packages (rhbz 864959)
- Consolidate netxen-firmware and ql2[123]xx-firmware packages (rhbz 864959)

* Tue Sep 25 2012 Josh Boyer <jwboyer@redhat.com>
- Update to latest upstream.  Adds marvell wifi updates (rhbz 858388)

* Tue Sep 18 2012 Josh Boyer <jwboyer@redhat.com>
- Add patch to create libertas subpackages from Daniel Drake (rhbz 853198)

* Fri Sep 07 2012 Josh Boyer <jwboyer@redhat.com> 20120720-0.2.git7560108
- Add epoch to iwl1000 subpackage to preserve upgrade patch (rhbz 855426)

* Fri Jul 20 2012 Josh Boyer <jwboyer@redhat.com> 20120720-0.1.git7560108
- Update to latest upstream.  Adds more realtek firmware and bcm4334

* Tue Jul 17 2012 Josh Boyer <jwboyer@redhat.com> 20120717-0.1.gitf1f86bb
- Update to latest upstream.  Adds updated realtek firmware

* Thu Jun 07 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.5.git375e954
- Bump release to get around koji

* Thu Jun 07 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.4.git375e954
- Drop udev requires.  Systemd now provides udev

* Tue Jun 05 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.3.git375e954
- Fix location of BuildRequires so git is inclued in the buildroot
- Create iwlXXXX-firmware subpackages (rhbz 828050)

* Thu May 10 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.1.git375e954
- Update to latest upstream.  Adds new bnx2x and radeon firmware

* Wed Apr 18 2012 Josh Boyer <jwboyer@redhat.com> 20120418-0.1.git85fbcaa
- Update to latest upstream.  Adds new rtl and ath firmware

* Wed Mar 21 2012 Dave Airlie <airlied@redhat.com> 20120206-0.3.git06c8f81
- use git to apply the radeon firmware

* Wed Mar 21 2012 Dave Airlie <airlied@redhat.com> 20120206-0.2.git06c8f81
- add radeon southern islands/trinity firmware

* Tue Feb 07 2012 Josh Boyer <jwboyer@redhat.com> 20120206-0.1.git06c8f81
- Update to latest upstream git snapshot.  Fixes rhbz 786937

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110731-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 04 2011 Tom Callaway <spot@fedoraproject.org> 20110731-2
- resolve conflict with netxen-firmware

* Wed Aug 03 2011 David Woodhouse <dwmw2@infradead.org> 20110731-1
- Latest firmware release with v1.3 ath9k firmware (#727702)

* Sun Jun 05 2011 Peter Lemenkov <lemenkov@gmail.com> 20110601-2
- Remove duplicated licensing files from /lib/firmware

* Wed Jun 01 2011 Dave Airlie <airlied@redhat.com> 20110601-1
- Latest firmware release with AMD llano support.

* Thu Mar 10 2011 Dave Airlie <airlied@redhat.com> 20110304-1
- update to latest upstream for radeon ni/cayman, drop nouveau fw we don't use it anymore

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 David Woodhouse <dwmw2@infradead.org> 20110125-1
- Update to linux-firmware-20110125 (new bnx2 firmware)

* Fri Jan 07 2011 Dave Airlie <airlied@redhat.com> 20101221-1
- rebase to upstream release + add new radeon NI firmwares.

* Thu Aug 12 2010 Hicham HAOUARI <hicham.haouari@gmail.com> 20100806-4
- Really obsolete ueagle-atm4-firmware

* Thu Aug 12 2010 Hicham HAOUARI <hicham.haouari@gmail.com> 20100806-3
- Obsolete ueagle-atm4-firmware

* Fri Aug 06 2010 David Woodhouse <dwmw2@infradead.org> 20100806-2
- Remove duplicate radeon firmwares; they're upstream now

* Fri Aug 06 2010 David Woodhouse <dwmw2@infradead.org> 20100806-1
- Update to linux-firmware-20100806 (more legacy firmwares from kernel source)

* Fri Apr 09 2010 Dave Airlie <airlied@redhat.com> 20100106-4
- Add further radeon firmwares

* Wed Feb 10 2010 Dave Airlie <airlied@redhat.com> 20100106-3
- add radeon RLC firmware - submitted upstream to dwmw2 already.

* Tue Feb 09 2010 Ben Skeggs <bskeggs@redhat.com> 20090106-2
- Add firmware needed for nouveau to operate correctly (this is Fedora
  only - do not upstream yet - we just moved it here from Fedora kernel)

* Wed Jan 06 2010 David Woodhouse <David.Woodhouse@intel.com> 20090106-1
- Update

* Fri Aug 21 2009 David Woodhouse <David.Woodhouse@intel.com> 20090821-1
- Update, fix typos, remove some files which conflict with other packages.

* Thu Mar 19 2009 David Woodhouse <David.Woodhouse@intel.com> 20090319-1
- First standalone kernel-firmware package.
