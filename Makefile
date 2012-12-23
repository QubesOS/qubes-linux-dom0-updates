stage0:
	rpmbuild --rebuild --define "_rpmdir rpm/" xorg-x11-util-macros-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" libpciaccess-*.src.rpm

stage1:
	rpmbuild --rebuild --define "_rpmdir rpm/" mtdev-*.src.rpm
	MAKELEVEL= rpmbuild --rebuild --define "_rpmdir rpm/" libdrm-*.src.rpm 
	rpmbuild --rebuild --define "_rpmdir rpm/" libXfont-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" xorg-x11-proto-devel-*.src.rpm
	./fix-and-build-driver.sh libXi-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" pixman-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" llvm-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" pmount-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" linux-firmware-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" netxen-firmware-*.src.rpm

stage2:
	rpmbuild --rebuild --define "_rpmdir rpm/" mesa-*.src.rpm 

stage3:
	rpmbuild --rebuild --define "_rpmdir rpm/" xorg-x11-server-*.src.rpm

stage4:
	for drv in xorg-x11-drv-*.src.rpm; do \
	    ./fix-and-build-driver.sh $$drv || exit 1; \
	done
	rpmbuild -bb --define "_rpmdir rpm/" xorg-x11-drivers.spec
	# rebuild with newer xorg-x11-server-devel
	rpmbuild --rebuild --define "_rpmdir rpm/" mesa-*.src.rpm 

update-repo-installer:
	ln -f rpm/noarch/*.rpm ../installer/yum/dom0-updates/rpm/
	ln -f rpm/x86_64/*.rpm ../installer/yum/dom0-updates/rpm/

update-repo-current:
	ln -f rpm/noarch/*.rpm ../yum/current-release/current/dom0/rpm/
	ln -f rpm/x86_64/*.rpm ../yum/current-release/current/dom0/rpm/

update-repo-current-testing:
	ln -f rpm/noarch/*.rpm ../yum/current-release/current-testing/dom0/rpm/
	ln -f rpm/x86_64/*.rpm ../yum/current-release/current-testing/dom0/rpm/

update-repo-unstable:
	ln -f rpm/noarch/*.rpm ../yum/current-release/unstable/dom0/rpm/
	ln -f rpm/x86_64/*.rpm ../yum/current-release/unstable/dom0/rpm/

clean:

