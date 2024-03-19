#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v4
# autospec commit: f4bef72
#
Name     : gnome-bluetooth
Version  : 46.0
Release  : 35
URL      : https://download.gnome.org/sources/gnome-bluetooth/46/gnome-bluetooth-46.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-bluetooth/46/gnome-bluetooth-46.0.tar.xz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n gnome-bluetooth-46.0
cd %{_builddir}/gnome-bluetooth-46.0
pushd ..
cp -a gnome-bluetooth-46.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710890320
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-bluetooth
cp %{_builddir}/gnome-bluetooth-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-bluetooth/b47456e2c1f38c40346ff00db976a2badf36b5e3 || :
cp %{_builddir}/gnome-bluetooth-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/gnome-bluetooth/545f380fb332eb41236596500913ff8d582e3ead || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-bluetooth-3.0
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/bluetooth-sendto
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
/V3/usr/lib64/libgnome-bluetooth-3.0.so.13.2.0
/V3/usr/lib64/libgnome-bluetooth-ui-3.0.so.13.2.0
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

