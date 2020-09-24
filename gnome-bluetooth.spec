#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-bluetooth
Version  : 3.34.2
Release  : 22
URL      : https://download.gnome.org/sources/gnome-bluetooth/3.34/gnome-bluetooth-3.34.2.tar.xz
Source0  : https://download.gnome.org/sources/gnome-bluetooth/3.34/gnome-bluetooth-3.34.2.tar.xz
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
BuildRequires : glibc-bin
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : libcanberra-dev
BuildRequires : libnotify-dev
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libnotify)

%description
# GNOME Bluetooth
gnome-bluetooth is collection of widgets for applications that want
to select Bluetooth devices. It is also used by GNOME session
components such as the Settings and gnome-shell.

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
%setup -q -n gnome-bluetooth-3.34.2
cd %{_builddir}/gnome-bluetooth-3.34.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600963242
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-bluetooth
cp %{_builddir}/gnome-bluetooth-3.34.2/COPYING %{buildroot}/usr/share/package-licenses/gnome-bluetooth/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/gnome-bluetooth-3.34.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/gnome-bluetooth/545f380fb332eb41236596500913ff8d582e3ead
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-bluetooth2

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bluetooth-sendto

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GnomeBluetooth-1.0.typelib
/usr/share/applications/bluetooth-sendto.desktop
/usr/share/gir-1.0/*.gir
/usr/share/gnome-bluetooth/pin-code-database.xml
/usr/share/icons/hicolor/16x16/apps/bluetooth.png
/usr/share/icons/hicolor/16x16/status/bluetooth-active.png
/usr/share/icons/hicolor/16x16/status/bluetooth-disabled.png
/usr/share/icons/hicolor/16x16/status/bluetooth-paired.png
/usr/share/icons/hicolor/22x22/apps/bluetooth.png
/usr/share/icons/hicolor/22x22/status/bluetooth-active.png
/usr/share/icons/hicolor/22x22/status/bluetooth-disabled.png
/usr/share/icons/hicolor/22x22/status/bluetooth-paired.png
/usr/share/icons/hicolor/24x24/apps/bluetooth.png
/usr/share/icons/hicolor/24x24/status/bluetooth-active.png
/usr/share/icons/hicolor/24x24/status/bluetooth-disabled.png
/usr/share/icons/hicolor/24x24/status/bluetooth-paired.png
/usr/share/icons/hicolor/32x32/apps/bluetooth.png
/usr/share/icons/hicolor/32x32/status/bluetooth-active.png
/usr/share/icons/hicolor/32x32/status/bluetooth-disabled.png
/usr/share/icons/hicolor/32x32/status/bluetooth-paired.png
/usr/share/icons/hicolor/48x48/apps/bluetooth.png
/usr/share/icons/hicolor/48x48/status/bluetooth-active.png
/usr/share/icons/hicolor/48x48/status/bluetooth-disabled.png
/usr/share/icons/hicolor/scalable/apps/bluetooth.svg
/usr/share/icons/hicolor/scalable/status/bluetooth-paired.svg

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-bluetooth/bluetooth-chooser-button.h
/usr/include/gnome-bluetooth/bluetooth-chooser-combo.h
/usr/include/gnome-bluetooth/bluetooth-chooser.h
/usr/include/gnome-bluetooth/bluetooth-client.h
/usr/include/gnome-bluetooth/bluetooth-enums.h
/usr/include/gnome-bluetooth/bluetooth-filter-widget.h
/usr/include/gnome-bluetooth/bluetooth-settings-widget.h
/usr/include/gnome-bluetooth/bluetooth-utils.h
/usr/lib64/libgnome-bluetooth.so
/usr/lib64/pkgconfig/gnome-bluetooth-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgnome-bluetooth.so.13
/usr/lib64/libgnome-bluetooth.so.13.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-bluetooth/545f380fb332eb41236596500913ff8d582e3ead
/usr/share/package-licenses/gnome-bluetooth/b47456e2c1f38c40346ff00db976a2badf36b5e3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bluetooth-sendto.1

%files locales -f gnome-bluetooth2.lang
%defattr(-,root,root,-)

