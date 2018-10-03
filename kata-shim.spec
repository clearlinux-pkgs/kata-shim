#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kata-shim
Version  : 1.3.0
Release  : 9
URL      : https://github.com/kata-containers/shim/archive/1.3.0.tar.gz
Source0  : https://github.com/kata-containers/shim/archive/1.3.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MIT
Requires: kata-shim-data = %{version}-%{release}
Requires: kata-shim-libexec = %{version}-%{release}
Requires: kata-shim-license = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0001-add-fake-autogen.patch

%description
This is a work-in-progress HTTP/2 implementation for Go.
It will eventually live in the Go standard library and won't require
any changes to your code to use.  It will just be automatic.

%package data
Summary: data components for the kata-shim package.
Group: Data

%description data
data components for the kata-shim package.


%package libexec
Summary: libexec components for the kata-shim package.
Group: Default

%description libexec
libexec components for the kata-shim package.


%package license
Summary: license components for the kata-shim package.
Group: Default

%description license
license components for the kata-shim package.


%prep
%setup -q -n shim-1.3.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538420078
%autogen --disable-static ;export GOPATH="${PWD}/gopath/" \
;mkdir -p "${GOPATH}/src/github.com/kata-containers/" \
;ln -sf "${PWD}" "${GOPATH}/src/github.com/kata-containers/shim" \
;cd "${GOPATH}/src/github.com/kata-containers/shim"
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1538420078
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kata-shim
cp LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/LICENSE
cp vendor/github.com/Azure/go-ansiterm/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_Azure_go-ansiterm_LICENSE
cp vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_davecgh_go-spew_LICENSE
cp vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_docker_docker_LICENSE
cp vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_docker_docker_NOTICE
cp vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_gogo_protobuf_LICENSE
cp vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_golang_protobuf_LICENSE
cp vendor/github.com/kata-containers/agent/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_kata-containers_agent_LICENSE
cp vendor/github.com/kr/pty/License %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_kr_pty_License
cp vendor/github.com/mdlayher/vsock/LICENSE.md %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_mdlayher_vsock_LICENSE.md
cp vendor/github.com/moby/moby/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_moby_moby_LICENSE
cp vendor/github.com/moby/moby/NOTICE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_moby_moby_NOTICE
cp vendor/github.com/opencontainers/runtime-spec/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_opencontainers_runtime-spec_LICENSE
cp vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_pmezard_go-difflib_LICENSE
cp vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_sirupsen_logrus_LICENSE
cp vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_github.com_stretchr_testify_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_golang.org_x_net_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_golang.org_x_sys_LICENSE
cp vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_golang.org_x_text_LICENSE
cp vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_google.golang.org_genproto_LICENSE
cp vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/kata-shim/vendor_google.golang.org_grpc_LICENSE
%make_install LIBEXECDIR=%{buildroot}//usr/libexec/

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/package-licenses/kata-shim/vendor_github.com_docker_docker_NOTICE
/usr/share/package-licenses/kata-shim/vendor_github.com_kr_pty_License
/usr/share/package-licenses/kata-shim/vendor_github.com_moby_moby_NOTICE

%files libexec
%defattr(-,root,root,-)
/usr/libexec/kata-containers/kata-shim

%files license
%defattr(-,root,root,-)
/usr/share/package-licenses/kata-shim/LICENSE
/usr/share/package-licenses/kata-shim/vendor_github.com_Azure_go-ansiterm_LICENSE
/usr/share/package-licenses/kata-shim/vendor_github.com_davecgh_go-spew_LICENSE
/usr/share/package-licenses/kata-shim/vendor_github.com_docker_docker_LICENSE
/usr/share/package-licenses/kata-shim/vendor_github.com_gogo_protobuf_LICENSE
/usr/share/package-licenses/kata-shim/vendor_github.com_golang_protobuf_LICENSE
/usr/share/package-licenses/kata-shim/vendor_github.com_kata-containers_agent_LICENSE
/usr/share/package-licenses/kata-shim/vendor_github.com_mdlayher_vsock_LICENSE.md
/usr/share/package-licenses/kata-shim/vendor_github.com_moby_moby_LICENSE
/usr/share/package-licenses/kata-shim/vendor_github.com_opencontainers_runtime-spec_LICENSE
/usr/share/package-licenses/kata-shim/vendor_github.com_pmezard_go-difflib_LICENSE
/usr/share/package-licenses/kata-shim/vendor_github.com_sirupsen_logrus_LICENSE
/usr/share/package-licenses/kata-shim/vendor_github.com_stretchr_testify_LICENSE
/usr/share/package-licenses/kata-shim/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/kata-shim/vendor_golang.org_x_net_LICENSE
/usr/share/package-licenses/kata-shim/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/kata-shim/vendor_golang.org_x_text_LICENSE
/usr/share/package-licenses/kata-shim/vendor_google.golang.org_genproto_LICENSE
/usr/share/package-licenses/kata-shim/vendor_google.golang.org_grpc_LICENSE
