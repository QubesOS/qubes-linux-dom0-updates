#!/bin/sh

if [ $1 ]; then
	KERNEL_VER=$1
else
	# Try to find kernel version
	KERNEL_PKG=`ls ../yum/qubes-dom0/rpm/ |grep kernel-[0-9]`
	if [ "$KERNEL_PKG" ]; then
		KERNEL_VER=$(echo $KERNEL_PKG | sed -e 's/kernel-//g;s/\.rpm//g')
	else
		echo "ERROR: Cannot find version of kernel for Qubes Dom0, provide it as parameter"
		exit 1
	fi
fi

if ! rpm -q kernel-devel-$KERNEL_VER; then
	echo "ERROR: Install kernel-devel package first!"
	exit 1
fi

rpmbuild --rebuild --define "_rpmdir rpm/" livna-config-display-*.src.rpm || exit 1
rpmbuild --rebuild --define "_rpmdir rpm/" xorg-x11-drv-nvidia-*.src.rpm || exit 1
rpmbuild --rebuild --define "_rpmdir rpm/" -D "kernels $KERNEL_VER" nvidia-kmod-*.src.rpm || exit 1
echo Done.
