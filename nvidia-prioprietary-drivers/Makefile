rpms:
	./nvidia_build.sh $(KERNEL_VER)
	# Sign all rpms - also this just downloaded
	# (dom0 has no keys to verify original signature)

sign:
	rpm --addsign rpm/x86_64/*.rpm

clean:
	rm *.src.rpm
	rm -rf rpm/
