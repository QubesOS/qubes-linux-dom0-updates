rpms:
	./nvidia_build.sh
	# Sign all rpms - also this just downloaded
	# (dom0 has no keys to verify original signature)
	# rpm pass additional argument directly as argv, so we must repeat
	# "gpg" name and add some dummy option at the end to ignore original "gpg"
	# added by rpm
	rpm --addsign --define "__gpg `which gpg` gpg --digest-algo SHA256 --comment" rpm/x86_64/*.rpm

clean:
	rm *.src.rpm
	rm -rf rpm/
