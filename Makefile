stage0:
	true

stage1:
	true

stage2:
	true

stage3:
	true

stage4:
	true

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

