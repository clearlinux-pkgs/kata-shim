#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kata-shim
Version  : 1.1.0
Release  : 4
URL      : https://github.com/kata-containers/shim/archive/1.1.0.tar.gz
Source0  : https://github.com/kata-containers/shim/archive/1.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MIT
Requires: kata-shim-bin
BuildRequires : go
Patch1: 0001-add-fake-autogen.patch

%description
This is a work-in-progress HTTP/2 implementation for Go.
It will eventually live in the Go standard library and won't require
any changes to your code to use.  It will just be automatic.

%package bin
Summary: bin components for the kata-shim package.
Group: Binaries

%description bin
bin components for the kata-shim package.


%prep
%setup -q -n shim-1.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533139151
%autogen --disable-static ;export GOPATH="${PWD}/gopath/" \
;mkdir -p "${GOPATH}/src/github.com/kata-containers/" \
;ln -sf "${PWD}" "${GOPATH}/src/github.com/kata-containers/shim" \
;cd "${GOPATH}/src/github.com/kata-containers/shim"
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1533139151
rm -rf %{buildroot}
%make_install LIBEXECDIR=%{buildroot}//usr/libexec/

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/kata-containers/kata-shim
