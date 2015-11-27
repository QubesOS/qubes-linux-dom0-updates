Name:		build-deps-qxl
Version:	1.0
Release:	1%{?dist}
Summary:	xorg-x11-drv-qxl is missing build requires in src.rpm metadata

Group:		System
License:	GPL

BuildRequires:	spice-server-devel >= 0.8.0

%description
xorg-x11-drv-qxl is missing build requires in src.rpm metadata, but spec file
have it set. Such situation isn't handled properly by Qubes Builder (but
actually it is broken package), so no need to be.
Add a dummy package, which just lists that requirements and build it before
acual xorg-x11-drv-qxl package.
