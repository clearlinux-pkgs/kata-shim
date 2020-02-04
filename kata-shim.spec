#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kata-shim
Version  : 1.10.0
Release  : 21
URL      : https://github.com/kata-containers/shim/archive/1.10.0/shim-1.10.0.tar.gz
Source0  : https://github.com/kata-containers/shim/archive/1.10.0/shim-1.10.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause GPL-2.0 ISC MIT MPL-2.0-no-copyleft-exception
Requires: kata-shim-libexec = %{version}-%{release}
Requires: kata-shim-license = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0001-add-fake-autogen.patch

%description
[![Build Status](https://travis-ci.org/kata-containers/shim.svg?branch=master)](https://travis-ci.org/kata-containers/shim)
[![codecov](https://codecov.io/gh/kata-containers/shim/branch/master/graph/badge.svg)](https://codecov.io/gh/kata-containers/shim)

%package libexec
Summary: libexec components for the kata-shim package.
Group: Default
Requires: kata-shim-license = %{version}-%{release}

%description libexec
libexec components for the kata-shim package.


%package license
Summary: license components for the kata-shim package.
Group: Default

%description license
license components for the kata-shim package.


%prep
%setup -q -n shim-1.10.0
cd %{_builddir}/shim-1.10.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580840956
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static ;export GOPATH="${PWD}/gopath/" \
;mkdir -p "${GOPATH}/src/github.com/kata-containers/" \
;ln -sf "${PWD}" "${GOPATH}/src/github.com/kata-containers/shim" \
;cd "${GOPATH}/src/github.com/kata-containers/shim"
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1580840956
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kata-shim
cp %{_builddir}/shim-1.10.0/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/shim-1.10.0/vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/836ef1b46953afdb78ce3929bc6831ca83620b65
cp %{_builddir}/shim-1.10.0/vendor/github.com/codahale/hdrhistogram/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/23d68de7aa2faedcbe131e4ff5b1fdd25af585dd
cp %{_builddir}/shim-1.10.0/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/0e9ad2a801d95231296b0b613db53147258260b1
cp %{_builddir}/shim-1.10.0/vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/878e7d86573d6c8ff65d2eaab294734b3f4d3d81
cp %{_builddir}/shim-1.10.0/vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/package-licenses/kata-shim/ea2531724c168e1e53717622d1bf302554225f2b
cp %{_builddir}/shim-1.10.0/vendor/github.com/docker/docker/contrib/selinux-fedora-24/docker-engine-selinux/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/shim-1.10.0/vendor/github.com/docker/docker/contrib/selinux-oraclelinux-7/docker-engine-selinux/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
cp %{_builddir}/shim-1.10.0/vendor/github.com/docker/docker/contrib/syntax/vim/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/cc299c1fe1c186e7842662c4e23d4fa067262be1
cp %{_builddir}/shim-1.10.0/vendor/github.com/docker/docker/pkg/symlink/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/kata-shim/a71b5152bb7c0d188273009e050644a6788d4d4c
cp %{_builddir}/shim-1.10.0/vendor/github.com/docker/docker/pkg/symlink/LICENSE.BSD %{buildroot}/usr/share/package-licenses/kata-shim/bb8bbeae44ef2e1eb6f8fec601a6234d4c5a51f7
cp %{_builddir}/shim-1.10.0/vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/06b27345acae9303e13dde9974d2b2e318b05989
cp %{_builddir}/shim-1.10.0/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/9d6e7962016b087c7c6c7b485f84aca70fe93242
cp %{_builddir}/shim-1.10.0/vendor/github.com/grpc-ecosystem/grpc-opentracing/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/cc9d362955ac00e08a474b658a935cd51da52007
cp %{_builddir}/shim-1.10.0/vendor/github.com/hashicorp/yamux/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/784701375491309231e6d26850c410e36c246d15
cp %{_builddir}/shim-1.10.0/vendor/github.com/kata-containers/agent/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/shim-1.10.0/vendor/github.com/kr/pty/License %{buildroot}/usr/share/package-licenses/kata-shim/37a5e9e1835e9b179f9d7175f25c3349d47b76f8
cp %{_builddir}/shim-1.10.0/vendor/github.com/mdlayher/vsock/LICENSE.md %{buildroot}/usr/share/package-licenses/kata-shim/a399653ce1cf03767aa146924f33db27bfdd16ac
cp %{_builddir}/shim-1.10.0/vendor/github.com/moby/moby/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/376caa2cd54c4196280157d071524614350e7ce8
cp %{_builddir}/shim-1.10.0/vendor/github.com/moby/moby/NOTICE %{buildroot}/usr/share/package-licenses/kata-shim/321794b769bbcd8144c089890e3c302d1f7f1353
cp %{_builddir}/shim-1.10.0/vendor/github.com/moby/moby/contrib/selinux-fedora-24/docker-engine-selinux/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/shim-1.10.0/vendor/github.com/moby/moby/contrib/selinux-oraclelinux-7/docker-engine-selinux/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/shim-1.10.0/vendor/github.com/moby/moby/contrib/selinux/docker-engine-selinux/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
cp %{_builddir}/shim-1.10.0/vendor/github.com/moby/moby/contrib/syntax/vim/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/cc299c1fe1c186e7842662c4e23d4fa067262be1
cp %{_builddir}/shim-1.10.0/vendor/github.com/moby/moby/pkg/symlink/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/kata-shim/fb1bf49ddf574b8e6d1863539b1a08ec3b66d05e
cp %{_builddir}/shim-1.10.0/vendor/github.com/moby/moby/pkg/symlink/LICENSE.BSD %{buildroot}/usr/share/package-licenses/kata-shim/97f81fec217d60daba14acea42c77ad9550659a0
cp %{_builddir}/shim-1.10.0/vendor/github.com/opencontainers/runtime-spec/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/552b909d29bd260c886142a969b462c85f976dcd
cp %{_builddir}/shim-1.10.0/vendor/github.com/opentracing/opentracing-go/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/75b05723a69674cde02ec34aac00db38fbbabccd
cp %{_builddir}/shim-1.10.0/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
cp %{_builddir}/shim-1.10.0/vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/cd3e4d932cee20da681e6b3bee8139cb4f734034
cp %{_builddir}/shim-1.10.0/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/shim-1.10.0/vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/5e630aeef4ff3e9b29a46622496b3fbbf5d7fe56
cp %{_builddir}/shim-1.10.0/vendor/github.com/uber/jaeger-client-go/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/shim-1.10.0/vendor/github.com/uber/jaeger-lib/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/shim-1.10.0/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/shim-1.10.0/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/shim-1.10.0/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/shim-1.10.0/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/shim-1.10.0/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/shim-1.10.0/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/2b8b815229aa8a61e483fb4ba0588b8b6c491890
%make_install LIBEXECDIR=/usr/libexec/

%files
%defattr(-,root,root,-)

%files libexec
%defattr(-,root,root,-)
/usr/libexec/kata-containers/kata-shim

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kata-shim/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/kata-shim/06b27345acae9303e13dde9974d2b2e318b05989
/usr/share/package-licenses/kata-shim/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
/usr/share/package-licenses/kata-shim/0e9ad2a801d95231296b0b613db53147258260b1
/usr/share/package-licenses/kata-shim/23d68de7aa2faedcbe131e4ff5b1fdd25af585dd
/usr/share/package-licenses/kata-shim/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/kata-shim/321794b769bbcd8144c089890e3c302d1f7f1353
/usr/share/package-licenses/kata-shim/376caa2cd54c4196280157d071524614350e7ce8
/usr/share/package-licenses/kata-shim/37a5e9e1835e9b179f9d7175f25c3349d47b76f8
/usr/share/package-licenses/kata-shim/552b909d29bd260c886142a969b462c85f976dcd
/usr/share/package-licenses/kata-shim/5e630aeef4ff3e9b29a46622496b3fbbf5d7fe56
/usr/share/package-licenses/kata-shim/75b05723a69674cde02ec34aac00db38fbbabccd
/usr/share/package-licenses/kata-shim/784701375491309231e6d26850c410e36c246d15
/usr/share/package-licenses/kata-shim/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/kata-shim/836ef1b46953afdb78ce3929bc6831ca83620b65
/usr/share/package-licenses/kata-shim/878e7d86573d6c8ff65d2eaab294734b3f4d3d81
/usr/share/package-licenses/kata-shim/97f81fec217d60daba14acea42c77ad9550659a0
/usr/share/package-licenses/kata-shim/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/kata-shim/9d6e7962016b087c7c6c7b485f84aca70fe93242
/usr/share/package-licenses/kata-shim/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/kata-shim/a399653ce1cf03767aa146924f33db27bfdd16ac
/usr/share/package-licenses/kata-shim/a71b5152bb7c0d188273009e050644a6788d4d4c
/usr/share/package-licenses/kata-shim/bb8bbeae44ef2e1eb6f8fec601a6234d4c5a51f7
/usr/share/package-licenses/kata-shim/cc299c1fe1c186e7842662c4e23d4fa067262be1
/usr/share/package-licenses/kata-shim/cc9d362955ac00e08a474b658a935cd51da52007
/usr/share/package-licenses/kata-shim/cd3e4d932cee20da681e6b3bee8139cb4f734034
/usr/share/package-licenses/kata-shim/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/kata-shim/ea2531724c168e1e53717622d1bf302554225f2b
/usr/share/package-licenses/kata-shim/fb1bf49ddf574b8e6d1863539b1a08ec3b66d05e
