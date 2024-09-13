#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v19
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kirigami-gallery
Version  : 24.08.1
Release  : 28
URL      : https://download.kde.org/stable/release-service/24.08.1/src/kirigami-gallery-24.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.1/src/kirigami-gallery-24.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.1/src/kirigami-gallery-24.08.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: kirigami-gallery-bin = %{version}-%{release}
Requires: kirigami-gallery-data = %{version}-%{release}
Requires: kirigami-gallery-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Kirigami Gallery
Example application which uses all features from kirigami, including links to the sourcecode, tips on how to use the components and links to the corresponding HIG pages and code examples on invent.

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kirigami-gallery-24.08.1
cd %{_builddir}/kirigami-gallery-24.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726255173
mkdir -p clr-build
pushd clr-build
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

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
export SOURCE_DATE_EPOCH=1726255173
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kirigami-gallery
cp %{_builddir}/kirigami-gallery-%{version}/LICENSE.LGPL-2 %{buildroot}/usr/share/package-licenses/kirigami-gallery/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
export GOAMD64=v2
GOAMD64=v2
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
/usr/share/locale/da/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/de/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/el/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/es/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/et/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/he/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/it/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kirigamigallery_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kirigamigallery_qt.qm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kirigami-gallery/ba8966e2473a9969bdcab3dc82274c817cfd98a1
