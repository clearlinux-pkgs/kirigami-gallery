#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kirigami-gallery
Version  : 20.04.0
Release  : 18
URL      : https://download.kde.org/stable/release-service/20.04.0/src/kirigami-gallery-20.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.0/src/kirigami-gallery-20.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.0/src/kirigami-gallery-20.04.0.tar.xz.sig
Summary  : Gallery application built using Kirigami
Group    : Development/Tools
License  : LGPL-2.0
Requires: kirigami-gallery-bin = %{version}-%{release}
Requires: kirigami-gallery-data = %{version}-%{release}
Requires: kirigami-gallery-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
# Kirigami Gallery
Example application which uses all features from kirigami, including links to the sourcecode, tips on how to use the components and links to the corresponding HIG pages and code examples on cgit

%package bin
Summary: bin components for the kirigami-gallery package.
Group: Binaries
Requires: kirigami-gallery-data = %{version}-%{release}
Requires: kirigami-gallery-license = %{version}-%{release}

%description bin
bin components for the kirigami-gallery package.


%package data
Summary: data components for the kirigami-gallery package.
Group: Data

%description data
data components for the kirigami-gallery package.


%package license
Summary: license components for the kirigami-gallery package.
Group: Default

%description license
license components for the kirigami-gallery package.


%prep
%setup -q -n kirigami-gallery-20.04.0
cd %{_builddir}/kirigami-gallery-20.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587686420
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1587686420
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kirigami-gallery
cp %{_builddir}/kirigami-gallery-20.04.0/LICENSE.LGPL-2 %{buildroot}/usr/share/package-licenses/kirigami-gallery/ba8966e2473a9969bdcab3dc82274c817cfd98a1
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kirigami2gallery

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kirigami2.gallery.desktop
/usr/share/locale/ca/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/de/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/el/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/es/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/et/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/it/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/metainfo/org.kde.kirigami2.gallery.appdata.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kirigami-gallery/ba8966e2473a9969bdcab3dc82274c817cfd98a1
