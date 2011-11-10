libdrm: 
	rpmbuild --rebuild --define "_rpmdir rpm/" libdrm-*.src.rpm 

xorg-drv-intel: 
	rpmbuild --rebuild --define "_rpmdir rpm/" xorg-x11-drv-intel-*.src.rpm 

mesa:
	rpmbuild --rebuild --define "_rpmdir rpm/" llvm-*.src.rpm
	rpmbuild --rebuild --define "_rpmdir rpm/" mesa-*.src.rpm 

update-repo-installer:
	ln -f rpm/noarch/*.rpm ../installer/yum/dom0-updates/rpm/
	ln -f rpm/x86_64/*.rpm ../installer/yum/dom0-updates/rpm/

clean:

