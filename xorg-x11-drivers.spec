Summary: X.Org X11 driver installation package
Name: xorg-x11-drivers
Version: 7.4
Release: 8%{?dist}
License: MIT
Group: User Interface/X Hardware Support

# Xorg is not (yet) buildable for s390.  When it is, we'll probably only
# want dummy and void anyway.  Maybe evdev for uinput stuff?
ExcludeArch: s390 s390x %{?rhel:ppc ppc64}

# Notable things missing:
# - imstt, not packaged yet, probably ppc only
# - impact, since we don't have a mips port
# - vermilion, the hardware is fictional
# - poulsbo, likewise
# - ark/chips/s3/tseng/vga, here's a nickel.

# relevant hardware 

Requires: xorg-x11-drv-ast
Requires: xorg-x11-drv-ati
Requires: xorg-x11-drv-cirrus
Requires: xorg-x11-drv-dummy
Requires: xorg-x11-drv-evdev
Requires: xorg-x11-drv-fbdev
Requires: xorg-x11-drv-mga
Requires: xorg-x11-drv-modesetting
Requires: xorg-x11-drv-nouveau
#Requires: xorg-x11-drv-qxl
Requires: xorg-x11-drv-synaptics
Requires: xorg-x11-drv-v4l
Requires: xorg-x11-drv-vesa
Requires: xorg-x11-drv-void
Requires: xorg-x11-drv-wacom

# So far intel is onboard-only.
%ifarch %{ix86} x86_64 ia64
Requires: xorg-x11-drv-intel
%endif

# vmware soft drivers.  yes, vmmouse really isn't ia64-enabled yet.
%ifarch %{ix86} x86_64 ia64
#Requires: xorg-x11-drv-vmware
%endif
%ifarch %{ix86} x86_64
#Requires: xorg-x11-drv-vmmouse
%endif

# irrelevant hardware

%if !0%{?rhel}

Requires: xorg-x11-drv-apm
Requires: xorg-x11-drv-glint
Requires: xorg-x11-drv-i128
Requires: xorg-x11-drv-i740
Requires: xorg-x11-drv-keyboard
Requires: xorg-x11-drv-mach64
Requires: xorg-x11-drv-mouse
Requires: xorg-x11-drv-nv
Requires: xorg-x11-drv-r128
Requires: xorg-x11-drv-rendition
Requires: xorg-x11-drv-s3virge
Requires: xorg-x11-drv-savage
Requires: xorg-x11-drv-siliconmotion
Requires: xorg-x11-drv-sis
Requires: xorg-x11-drv-sisusb
Requires: xorg-x11-drv-tdfx
Requires: xorg-x11-drv-trident
Requires: xorg-x11-drv-voodoo

# cyrix and nsc used to be here too, but are deprecated upstream and
# should eventually get folded into -geode.
%ifarch %{ix86}
Requires: xorg-x11-drv-geode
%endif

# This chipset has long since been EOLd, and afaik was only ever in x86 laptops
%ifarch %{ix86}
Requires: xorg-x11-drv-neomagic
%endif

# Thus far via chips are only on x86 and amd64 motherboards.  This might be
# the driver that ends up supporting the S3 Chrome cards, so don't be
# surprised if this changes.
%ifarch %{ix86} x86_64
Requires: xorg-x11-drv-openchrome
%endif

# Sun kit, sparc-only.
%ifarch sparc sparcv9 sparc64
Requires: xorg-x11-drv-suntcx
Requires: xorg-x11-drv-suncg3
Requires: xorg-x11-drv-suncg6
Requires: xorg-x11-drv-suncg14
Requires: xorg-x11-drv-sunffb
Requires: xorg-x11-drv-sunleo
Requires: xorg-x11-drv-sunbw2
%endif

# ARM kit
%ifarch %{arm}
Requires: xorg-x11-drv-omapfb
%endif
%endif

%description
The purpose of this package is to require all of the individual X.Org
driver rpms, to allow the OS installation software to install all drivers
all at once, without having to track which individual drivers are present
on each architecture.  By installing this package, it forces all of the
individual driver packages to be installed.

%prep
%build
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%changelog
* Mon Apr 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 7.4-8
- Add options for ARM

* Wed Mar 21 2012 Adam Jackson <ajax@redhat.com> 7.4-7
- More %%rhel conditionals
- Add -modesetting

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Adam Jackson <ajax@redhat.com> 7.4-5
- Reorganize and conditionalize for %%rhel

* Fri Oct 14 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.4-4
- Block penmount and elographics too. Penmount is unmaintained, elographics
  is maintained but may not work with the latest Xorg.

* Tue Sep 27 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.4-3
- Remove aiptek, acecad, fpit, hyperpen, penmount, mutouch. They are not
  maintained upstream anymore.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 04 2010 Adam Jackson <ajax@redhat.com> 7.4-1
- Add qxl

* Tue Mar 09 2010 Peter Hutterer <peter.hutterer@redhat.com> 7.3-14
- Wacom driver is now xorg-x11-drv-wacom.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Kristian Høgsberg <krh@redhat.com> - 7.3-12
- Rename i810 to intel.

* Thu Feb 26 2009 Dave Airlie <airlied@redhat.com> 7.3-11
- remove diamondtouch + wiimote

* Thu Feb 19 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.3-10
- s/synaptics/xorg-x11-drv-synaptics/.
- Remove calcomp, citron, digitaledge, dmc, dynapro, jamstudio, magellan,
  microtouch, palmax, spaceorb, summa, tek4957, ur98. Nobody uses them.

* Mon Aug 11 2008 Adam Jackson <ajax@redhat.com> 7.3-9
- Add r128 and mach64.

* Wed Jul 16 2008 Adam Jackson <ajax@redhat.com> 7.3-8
- Tee hee, imstt isn't packaged yet.

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 7.3-7
- Comment cleanup.
- Add imstt to ppc, just for giggles.

* Tue Jul 15 2008 Warren Togami <wtogami@redhat.com> 7.3-6
- amd was renamed to geode

* Wed Jun 04 2008 Dennis Gilmore <dennis@ausil.us> 7.3-5
- add sparc drivers

* Fri Apr 04 2008 Adam Jackson <ajax@redhat.com> 7.3-4
- Remove -nsc and -cyrix.

* Mon Mar 03 2008 Adam Jackson <ajax@redhat.com> 7.3-3
- Drop magictouch, it can not work and can never have worked.

* Fri Feb 22 2008 Adam Jackson <ajax@redhat.com> 7.3-2
- xorg-x11-drv-diamondtouch.

* Mon Feb 18 2008 Adam Jackson <ajax@redhat.com> 7.3-1
- Superstition bump to 7.3.
- xorg-x11-drv-wiimote.
- Additional commentary about drivers that aren't included here.

* Wed Jan 09 2008 Adam Jackson <ajax@redhat.com> 7.2-11
- Drop avivo for being a dead end.
- Drop ark, chips, s3, and tseng for being unspeakably lame.

* Tue Nov 27 2007 Adam Jackson <ajax@redhat.com> 7.2-10
- :s/via/openchrome/

* Mon Oct 15 2007 Adam Jackson <ajax@redhat.com> 7.2-9
- Archify synaptics, it's not buildable most places.

* Fri Oct 12 2007 Jeremy Katz <katzj@redhat.com> 7.2-8
- Add avivo

* Fri Sep 07 2007 Adam Jackson <ajax@redhat.com> 7.2-7
- Add linuxwacom and synaptics to the default set.

* Fri May 11 2007 Adam Jackson <ajax@redhat.com> 7.2-6
- Add xorg-x11-drv-nouveau.  If this bothers you, uninstall the metapackage.

* Tue Mar 20 2007 Adam Jackson <ajax@redhat.com> 7.2-5
- Un-Require xorg-x11-drv-vga.

* Tue Feb 27 2007 Adam Jackson <ajax@redhat.com> 7.2-4
- Remove elo2300 and joystick for being utterly broken.

* Mon Feb 26 2007 Adam Jackson <ajax@redhat.com> 7.2-3
- Fix the i810 ifarch to include all the relevant arches.

* Mon Feb 19 2007 Adam Jackson <ajax@redhat.com> 7.2-2
- Package review feedback fixes: (#226573)
  - Remove URL, misleading
  - Remove the Obsoletes: xorg-x11
  - Fix License tag

* Sun Feb 18 2007 Adam Jackson <ajax@redhat.com> 7.2-1
- Superstition bump to 7.2
- ExcludeArch of s390{,x}
- Only ExclusiveArch those drivers that really are processor-specific
- Readd forgotten -tek4957

* Thu Oct 12 2006 Jeremy Katz <katzj@redhat.com> - 7.1-4
- mga not on ppc

* Mon Aug 21 2006 Adam Jackson <ajackson@redhat.com> 7.1-3
- Add cirrus to all arches
- Don't bother building this for s390{,x}

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 7.1-2.1
- rebuild

* Thu Jun 29 2006 Mike Harris <mharris@redhat.com> 7.1-2
- Regenerate driver list to match current rawhide X11R7.1 driver set.

* Wed Jun 21 2006 Mike Harris <mharris@redhat.com> 7.1-1
- Regenerate driver list to match current rawhide X11R7.1 driver set.

* Thu Feb 16 2006 Bill Nottingham <notting@redhat.com> 7.0-2
- uncomment (empty) file list so binary RPMs are built

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 7.0-1.1
- bump again for double-long bug on ppc(64)

* Thu Feb 09 2006 Mike Harris <mharris@redhat.com> 7.0-1
- Bumped version to 7.0-1
- Updated the driver list to match current rawhide, X11R7.0

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 0.99.2-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Nov 23 2005 Mike Harris <mharris@redhat.com> 0.99.2-4
- Add ur98 driver back, as it is part of X11R7 RC2

* Tue Nov 15 2005 Jeremy Katz <katzj@redhat.com> 0.99.2-3
- ur98 driver doesn't exist

* Tue Nov 15 2005 Jeremy Katz <katzj@redhat.com> 0.99.2-2
- add an obsoletes on xorg-x11 to get pulled in on upgrades

* Tue Nov 15 2005 Mike Harris <mharris@redhat.com> 0.99.2-1
- Initial build.
