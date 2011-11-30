
cd $(dirname $0)
CACHEDIR=$(mktemp -d ${TMPDIR:-/tmp}/yumcache.XXXXXX)

releasever=13
basearch=x86_64

yumconf=$(mktemp ${TMPDIR:-/tmp}/yum.conf.XXXXXX)

trap "rm -f $yumconf; rm -rf $CACHEDIR" EXIT

# Done this way to easier replace some values (just modify variable)
cat > $yumconf <<EOF
[main]
cachedir=$CACHEDIR
keepcache=0
gpgcheck=1
plugins=0
reposdir=
tsflags=nodocs

[rpmfusion-free]
name=RPM Fusion for Fedora $releasever - Nonfree
#baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/os/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-$releasever&arch=$basearch
enabled=1
metadata_expire=7d
gpgcheck=1
gpgkey=file://$PWD/../keys/rpmfusion-free-fedora-$releasever-primary

[rpmfusion-free-updates]
name=RPM Fusion for Fedora $releasever - Nonfree - Updates
#baseurl=http://download1.rpmfusion.org/free/fedora/updates/$releasever/$basearch/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-updates-released-$releasever&arch=$basearch
enabled=1
gpgcheck=1
gpgkey=file://$PWD/../keys/rpmfusion-free-fedora-$releasever-primary

[rpmfusion-free-source]
name=RPM Fusion for Fedora $releasever - Nonfree - Source
#baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/source/SRPMS/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-source-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
gpgcheck=1
gpgkey=file://$PWD/../keys/rpmfusion-free-fedora-$releasever-primary


[rpmfusion-free-updates-source]
name=RPM Fusion for Fedora $releasever - Nonfree - Updates Source
#baseurl=http://download1.rpmfusion.org/free/fedora/updates/$releasever/SRPMS/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-updates-released-source-$releasever&arch=$basearch
enabled=0
gpgcheck=1
gpgkey=file://$PWD/../keys/rpmfusion-free-fedora-$releasever-primary

[rpmfusion-nonfree]
name=RPM Fusion for Fedora $releasever - Nonfree
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/$basearch/os/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-fedora-$releasever&arch=$basearch
enabled=1
metadata_expire=7d
gpgcheck=1
gpgkey=file://$PWD/../keys/rpmfusion-nonfree-fedora-$releasever-primary

[rpmfusion-nonfree-updates]
name=RPM Fusion for Fedora $releasever - Nonfree - Updates
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/updates/$releasever/$basearch/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-fedora-updates-released-$releasever&arch=$basearch
enabled=1
gpgcheck=1
gpgkey=file://$PWD/../keys/rpmfusion-nonfree-fedora-$releasever-primary

[rpmfusion-nonfree-source]
name=RPM Fusion for Fedora $releasever - Nonfree - Source
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/source/SRPMS/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-fedora-source-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
gpgcheck=1
gpgkey=file://$PWD/../keys/rpmfusion-nonfree-fedora-$releasever-primary


[rpmfusion-nonfree-updates-source]
name=RPM Fusion for Fedora $releasever - Nonfree - Updates Source
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/updates/$releasever/SRPMS/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-fedora-updates-released-source-$releasever&arch=$basearch
enabled=0
gpgcheck=1
gpgkey=file://$PWD/../keys/rpmfusion-nonfree-fedora-$releasever-primary
EOF

yumdownloader -c $yumconf --source nvidia-kmod xorg-x11-drv-nvidia livna-config-display

if rpm -K *.rpm | grep -v pgp; then
	echo "ERROR: Unverified/Invalid packages found! Aborting"
	exit 1
fi
