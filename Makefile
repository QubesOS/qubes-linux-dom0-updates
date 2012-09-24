stage1:
	rpmbuild --rebuild --define "_rpmdir rpm/" libdrm-*.src.rpm 
	rpmbuild --rebuild --define "_rpmdir rpm/" xorg-x11-util-macros-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" llvm-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" kmodtool-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" pmount-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" linux-firmware-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" netxen-firmware-*.src.rpm

stage2:
	rpmbuild --rebuild --define "_rpmdir rpm/" xorg-x11-drv-intel-*.src.rpm 
	rpmbuild --rebuild --define "_rpmdir rpm/" xorg-x11-drv-nouveau-*.src.rpm 
	rpmbuild --rebuild --define "_rpmdir rpm/" xorg-x11-drv-ati-fixed-*.src.rpm 
	rpmbuild --rebuild --define "_rpmdir rpm/" mesa-*.src.rpm 

nvidia:
	$(MAKE) -C nvidia-prioprietary-drivers rpms

update-repo-installer:
	ln -f rpm/noarch/*.rpm ../installer/yum/dom0-updates/rpm/
	ln -f rpm/x86_64/*.rpm ../installer/yum/dom0-updates/rpm/

update-repo-current:
	ln -f rpm/noarch/*.rpm ../yum/current-release/current/dom0/rpm/
	ln -f rpm/x86_64/*.rpm ../yum/current-release/current/dom0/rpm/
	ln -f nvidia-prioprietary-drivers/rpm/noarch/*.rpm ../yum/current-release/current/dom0/rpm/
	ln -f nvidia-prioprietary-drivers/rpm/x86_64/*.rpm ../yum/current-release/current/dom0/rpm/

update-repo-current-testing:
	ln -f rpm/noarch/*.rpm ../yum/current-release/current-testing/dom0/rpm/
	ln -f rpm/x86_64/*.rpm ../yum/current-release/current-testing/dom0/rpm/
	ln -f nvidia-prioprietary-drivers/rpm/noarch/*.rpm ../yum/current-release/current-testing/dom0/rpm/
	ln -f nvidia-prioprietary-drivers/rpm/x86_64/*.rpm ../yum/current-release/current-testing/dom0/rpm/

update-repo-unstable:
	ln -f rpm/noarch/*.rpm ../yum/current-release/unstable/dom0/rpm/
	ln -f rpm/x86_64/*.rpm ../yum/current-release/unstable/dom0/rpm/
	ln -f nvidia-prioprietary-drivers/rpm/noarch/*.rpm ../yum/current-release/unstable/dom0/rpm/
	ln -f nvidia-prioprietary-drivers/rpm/x86_64/*.rpm ../yum/current-release/unstable/dom0/rpm/

clean:

