#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : time
Version  : 1.7
Release  : 3
URL      : http://ftp.gnu.org/gnu/time/time-1.7.tar.gz
Source0  : http://ftp.gnu.org/gnu/time/time-1.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: time-bin
Requires: time-doc
Patch1: build.patch

%description
`time' is a program that measures many of the CPU resources, such as
time and memory, that other programs use.  The GNU version can format
the output in arbitrary ways by using a printf-style format string to
include various resource measurements.  Some systems do not provide
much information about program resource use; `time' reports
unavailable information as zero values.

%package bin
Summary: bin components for the time package.
Group: Binaries

%description bin
bin components for the time package.


%package doc
Summary: doc components for the time package.
Group: Documentation

%description doc
doc components for the time package.


%prep
%setup -q -n time-1.7
%patch1 -p1

%build
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/time

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
