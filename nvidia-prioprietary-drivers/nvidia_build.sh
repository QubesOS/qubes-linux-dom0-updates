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

rpmbuild -D "kernels $KERNEL_VER" --rebuild nvidia-kmod-*.src.rpm  || exit 1
# Unfortunately --define _rpmdir doesn't work with --rebuild
RPMDIR=`rpm -E '%_rpmdir'`
mv $RPMDIR/$basearch/kmod-nvidia-$KERNEL_VER*rpm rpm/$basearch/ || exit 1
echo Done.
