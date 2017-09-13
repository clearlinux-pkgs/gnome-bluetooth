#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-bluetooth
Version  : 3.26.0
Release  : 4
URL      : https://download.gnome.org/sources/gnome-bluetooth/3.26/gnome-bluetooth-3.26.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-bluetooth/3.26/gnome-bluetooth-3.26.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gnome-bluetooth-bin
Requires: gnome-bluetooth-data
Requires: gnome-bluetooth-lib
Requires: gnome-bluetooth-locales
Requires: gnome-bluetooth-doc
BuildRequires : glibc-bin
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : libxml2-dev
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libudev)
BuildRequires : python3

%description
GNOME Bluetooth
===============
gnome-bluetooth is a fork of bluez-gnome focused on integration with
the GNOME desktop environment.

%package bin
Summary: bin components for the gnome-bluetooth package.
Group: Binaries
Requires: gnome-bluetooth-data

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
Requires: gnome-bluetooth-lib
Requires: gnome-bluetooth-bin
Requires: gnome-bluetooth-data
Provides: gnome-bluetooth-devel

%description dev
dev components for the gnome-bluetooth package.


%package doc
Summary: doc components for the gnome-bluetooth package.
Group: Documentation

%description doc
doc components for the gnome-bluetooth package.


%package lib
Summary: lib components for the gnome-bluetooth package.
Group: Libraries
Requires: gnome-bluetooth-data

%description lib
lib components for the gnome-bluetooth package.


%package locales
Summary: locales components for the gnome-bluetooth package.
Group: Default

%description locales
locales components for the gnome-bluetooth package.


%prep
%setup -q -n gnome-bluetooth-3.26.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505320191
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain builddir
ninja -v -C builddir

%install
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
/usr/share/icons/hicolor/16x16/apps/hicolor_apps_16x16_bluetooth.png
/usr/share/icons/hicolor/16x16/status/hicolor_status_16x16_bluetooth-active.png
/usr/share/icons/hicolor/16x16/status/hicolor_status_16x16_bluetooth-disabled.png
/usr/share/icons/hicolor/16x16/status/hicolor_status_16x16_bluetooth-paired.png
/usr/share/icons/hicolor/22x22/apps/hicolor_apps_22x22_bluetooth.png
/usr/share/icons/hicolor/22x22/status/hicolor_status_22x22_bluetooth-active.png
/usr/share/icons/hicolor/22x22/status/hicolor_status_22x22_bluetooth-disabled.png
/usr/share/icons/hicolor/22x22/status/hicolor_status_22x22_bluetooth-paired.png
/usr/share/icons/hicolor/24x24/apps/hicolor_apps_24x24_bluetooth.png
/usr/share/icons/hicolor/24x24/status/hicolor_status_24x24_bluetooth-active.png
/usr/share/icons/hicolor/24x24/status/hicolor_status_24x24_bluetooth-disabled.png
/usr/share/icons/hicolor/24x24/status/hicolor_status_24x24_bluetooth-paired.png
/usr/share/icons/hicolor/32x32/apps/hicolor_apps_32x32_bluetooth.png
/usr/share/icons/hicolor/32x32/status/hicolor_status_32x32_bluetooth-active.png
/usr/share/icons/hicolor/32x32/status/hicolor_status_32x32_bluetooth-disabled.png
/usr/share/icons/hicolor/32x32/status/hicolor_status_32x32_bluetooth-paired.png
/usr/share/icons/hicolor/48x48/apps/hicolor_apps_48x48_bluetooth.png
/usr/share/icons/hicolor/48x48/status/hicolor_status_48x48_bluetooth-active.png
/usr/share/icons/hicolor/48x48/status/hicolor_status_48x48_bluetooth-disabled.png
/usr/share/icons/hicolor/scalable/apps/hicolor_apps_scalable_bluetooth.svg
/usr/share/icons/hicolor/scalable/status/hicolor_status_scalable_bluetooth-paired.svg

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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgnome-bluetooth.so.13
/usr/lib64/libgnome-bluetooth.so.13.0.1

%files locales -f gnome-bluetooth2.lang
%defattr(-,root,root,-)

