#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-bluetooth
Version  : 42.4
Release  : 29
URL      : https://download.gnome.org/sources/gnome-bluetooth/42/gnome-bluetooth-42.4.tar.xz
Source0  : https://download.gnome.org/sources/gnome-bluetooth/42/gnome-bluetooth-42.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gnome-bluetooth-bin = %{version}-%{release}
Requires: gnome-bluetooth-data = %{version}-%{release}
Requires: gnome-bluetooth-lib = %{version}-%{release}
Requires: gnome-bluetooth-license = %{version}-%{release}
Requires: gnome-bluetooth-locales = %{version}-%{release}
Requires: gnome-bluetooth-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : dbus-python
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : gsound-dev
BuildRequires : pkgconfig(gsound)
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : upower-dev

%description
# GNOME Bluetooth
gnome-bluetooth is a helper library on top of the bluez daemon's D-Bus API. It used
to contain widgets for application developers but is now home to everything Bluetooth
related for the code GNOME desktop, and nothing pertinent to application developers.

%package bin
Summary: bin components for the gnome-bluetooth package.
Group: Binaries
Requires: gnome-bluetooth-data = %{version}-%{release}
Requires: gnome-bluetooth-license = %{version}-%{release}

%description bin
bin components for the gnome-bluetooth package.


%package data
Summary: data components for the gnome-bluetooth package.
Group: Data

%description data
data components for the gnome-bluetooth package.


%package dev
Summary: dev components for the gnome-bluetooth package.
Group: Development
Requires: gnome-bluetooth-lib = %{version}-%{release}
Requires: gnome-bluetooth-bin = %{version}-%{release}
Requires: gnome-bluetooth-data = %{version}-%{release}
Provides: gnome-bluetooth-devel = %{version}-%{release}
Requires: gnome-bluetooth = %{version}-%{release}

%description dev
dev components for the gnome-bluetooth package.


%package lib
Summary: lib components for the gnome-bluetooth package.
Group: Libraries
Requires: gnome-bluetooth-data = %{version}-%{release}
Requires: gnome-bluetooth-license = %{version}-%{release}

%description lib
lib components for the gnome-bluetooth package.


%package license
Summary: license components for the gnome-bluetooth package.
Group: Default

%description license
license components for the gnome-bluetooth package.


%package locales
Summary: locales components for the gnome-bluetooth package.
Group: Default

%description locales
locales components for the gnome-bluetooth package.


%package man
Summary: man components for the gnome-bluetooth package.
Group: Default

%description man
man components for the gnome-bluetooth package.


%prep
%setup -q -n gnome-bluetooth-42.4
cd %{_builddir}/gnome-bluetooth-42.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662486524
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-bluetooth
cp %{_builddir}/gnome-bluetooth-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-bluetooth/b47456e2c1f38c40346ff00db976a2badf36b5e3 || :
cp %{_builddir}/gnome-bluetooth-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/gnome-bluetooth/545f380fb332eb41236596500913ff8d582e3ead || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-bluetooth-3.0

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bluetooth-sendto

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GnomeBluetooth-3.0.typelib
/usr/share/applications/bluetooth-sendto.desktop
/usr/share/gir-1.0/*.gir
/usr/share/gnome-bluetooth-3.0/pin-code-database.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-bluetooth-3.0/bluetooth-settings-widget.h
/usr/lib64/libgnome-bluetooth-3.0.so
/usr/lib64/libgnome-bluetooth-ui-3.0.so
/usr/lib64/pkgconfig/gnome-bluetooth-3.0.pc
/usr/lib64/pkgconfig/gnome-bluetooth-ui-3.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgnome-bluetooth-3.0.so.13
/usr/lib64/libgnome-bluetooth-3.0.so.13.2.0
/usr/lib64/libgnome-bluetooth-ui-3.0.so.13
/usr/lib64/libgnome-bluetooth-ui-3.0.so.13.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-bluetooth/545f380fb332eb41236596500913ff8d582e3ead
/usr/share/package-licenses/gnome-bluetooth/b47456e2c1f38c40346ff00db976a2badf36b5e3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bluetooth-sendto.1

%files locales -f gnome-bluetooth-3.0.lang
%defattr(-,root,root,-)

