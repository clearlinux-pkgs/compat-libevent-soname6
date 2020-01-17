#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB86086848EF8686D (bin@azat.sh)
#
Name     : compat-libevent-soname6
Version  : 2.1.10.stable
Release  : 32
URL      : https://github.com/libevent/libevent/releases/download/release-2.1.10-stable/libevent-2.1.10-stable.tar.gz
Source0  : https://github.com/libevent/libevent/releases/download/release-2.1.10-stable/libevent-2.1.10-stable.tar.gz
Source1  : https://github.com/libevent/libevent/releases/download/release-2.1.10-stable/libevent-2.1.10-stable.tar.gz.asc
Summary  : libevent_pthreads adds pthreads-based threading support to libevent
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: compat-libevent-soname6-lib = %{version}-%{release}
Requires: compat-libevent-soname6-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : openssl-dev
BuildRequires : openssl-dev32
BuildRequires : openssl-lib32
BuildRequires : pkg-config
BuildRequires : sed
BuildRequires : zlib-dev32
Patch1: pcfiles.patch

%description
No detailed description available

%package lib
Summary: lib components for the compat-libevent-soname6 package.
Group: Libraries
Requires: compat-libevent-soname6-license = %{version}-%{release}

%description lib
lib components for the compat-libevent-soname6 package.


%package lib32
Summary: lib32 components for the compat-libevent-soname6 package.
Group: Default
Requires: compat-libevent-soname6-license = %{version}-%{release}

%description lib32
lib32 components for the compat-libevent-soname6 package.


%package license
Summary: license components for the compat-libevent-soname6 package.
Group: Default

%description license
license components for the compat-libevent-soname6 package.


%prep
%setup -q -n libevent-2.1.10-stable
cd %{_builddir}/libevent-2.1.10-stable
%patch1 -p1
pushd ..
cp -a libevent-2.1.10-stable build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579292956
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --disable-libevent-regress
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --disable-libevent-regress   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1579292956
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-libevent-soname6
cp %{_builddir}/libevent-2.1.10-stable/LICENSE %{buildroot}/usr/share/package-licenses/compat-libevent-soname6/0f375374b877550ade2e001905a1f9c9b7128714
cp %{_builddir}/libevent-2.1.10-stable/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/compat-libevent-soname6/cc31ae51223e291f3f7389a4c96b2cf4c1e62757
cp %{_builddir}/libevent-2.1.10-stable/cmake/Copyright.txt %{buildroot}/usr/share/package-licenses/compat-libevent-soname6/b7708e46727dc00ced77b6421d1f4b4e4045c12d
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/event_rpcgen.py
rm -f %{buildroot}/usr/include/evdns.h
rm -f %{buildroot}/usr/include/event.h
rm -f %{buildroot}/usr/include/event2/buffer.h
rm -f %{buildroot}/usr/include/event2/buffer_compat.h
rm -f %{buildroot}/usr/include/event2/bufferevent.h
rm -f %{buildroot}/usr/include/event2/bufferevent_compat.h
rm -f %{buildroot}/usr/include/event2/bufferevent_ssl.h
rm -f %{buildroot}/usr/include/event2/bufferevent_struct.h
rm -f %{buildroot}/usr/include/event2/dns.h
rm -f %{buildroot}/usr/include/event2/dns_compat.h
rm -f %{buildroot}/usr/include/event2/dns_struct.h
rm -f %{buildroot}/usr/include/event2/event-config.h
rm -f %{buildroot}/usr/include/event2/event.h
rm -f %{buildroot}/usr/include/event2/event_compat.h
rm -f %{buildroot}/usr/include/event2/event_struct.h
rm -f %{buildroot}/usr/include/event2/http.h
rm -f %{buildroot}/usr/include/event2/http_compat.h
rm -f %{buildroot}/usr/include/event2/http_struct.h
rm -f %{buildroot}/usr/include/event2/keyvalq_struct.h
rm -f %{buildroot}/usr/include/event2/listener.h
rm -f %{buildroot}/usr/include/event2/rpc.h
rm -f %{buildroot}/usr/include/event2/rpc_compat.h
rm -f %{buildroot}/usr/include/event2/rpc_struct.h
rm -f %{buildroot}/usr/include/event2/tag.h
rm -f %{buildroot}/usr/include/event2/tag_compat.h
rm -f %{buildroot}/usr/include/event2/thread.h
rm -f %{buildroot}/usr/include/event2/util.h
rm -f %{buildroot}/usr/include/event2/visibility.h
rm -f %{buildroot}/usr/include/evhttp.h
rm -f %{buildroot}/usr/include/evrpc.h
rm -f %{buildroot}/usr/include/evutil.h
rm -f %{buildroot}/usr/lib32/libevent.so
rm -f %{buildroot}/usr/lib32/libevent_core.so
rm -f %{buildroot}/usr/lib32/libevent_extra.so
rm -f %{buildroot}/usr/lib32/libevent_openssl.so
rm -f %{buildroot}/usr/lib32/libevent_pthreads.so
rm -f %{buildroot}/usr/lib32/pkgconfig/32libevent.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/32libevent_core.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/32libevent_extra.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/32libevent_openssl.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/32libevent_pthreads.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/libevent.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/libevent_core.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/libevent_extra.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/libevent_openssl.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/libevent_pthreads.pc
rm -f %{buildroot}/usr/lib64/libevent.so
rm -f %{buildroot}/usr/lib64/libevent_core.so
rm -f %{buildroot}/usr/lib64/libevent_extra.so
rm -f %{buildroot}/usr/lib64/libevent_openssl.so
rm -f %{buildroot}/usr/lib64/libevent_pthreads.so
rm -f %{buildroot}/usr/lib64/pkgconfig/libevent.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/libevent_core.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/libevent_extra.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/libevent_openssl.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/libevent_pthreads.pc

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libevent-2.1.so.6
/usr/lib64/libevent-2.1.so.6.0.4
/usr/lib64/libevent_core-2.1.so.6
/usr/lib64/libevent_core-2.1.so.6.0.4
/usr/lib64/libevent_extra-2.1.so.6
/usr/lib64/libevent_extra-2.1.so.6.0.4
/usr/lib64/libevent_openssl-2.1.so.6
/usr/lib64/libevent_openssl-2.1.so.6.0.4
/usr/lib64/libevent_pthreads-2.1.so.6
/usr/lib64/libevent_pthreads-2.1.so.6.0.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libevent-2.1.so.6
/usr/lib32/libevent-2.1.so.6.0.4
/usr/lib32/libevent_core-2.1.so.6
/usr/lib32/libevent_core-2.1.so.6.0.4
/usr/lib32/libevent_extra-2.1.so.6
/usr/lib32/libevent_extra-2.1.so.6.0.4
/usr/lib32/libevent_openssl-2.1.so.6
/usr/lib32/libevent_openssl-2.1.so.6.0.4
/usr/lib32/libevent_pthreads-2.1.so.6
/usr/lib32/libevent_pthreads-2.1.so.6.0.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-libevent-soname6/0f375374b877550ade2e001905a1f9c9b7128714
/usr/share/package-licenses/compat-libevent-soname6/b7708e46727dc00ced77b6421d1f4b4e4045c12d
/usr/share/package-licenses/compat-libevent-soname6/cc31ae51223e291f3f7389a4c96b2cf4c1e62757
