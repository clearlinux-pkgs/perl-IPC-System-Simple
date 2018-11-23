#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IPC-System-Simple
Version  : 1.25
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/P/PJ/PJF/IPC-System-Simple-1.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PJ/PJF/IPC-System-Simple-1.25.tar.gz
Summary  : 'Run commands simply, with detailed diagnostics'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IPC-System-Simple-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution IPC-System-Simple,
version 1.25:
Run commands simply, with detailed diagnostics

%package dev
Summary: dev components for the perl-IPC-System-Simple package.
Group: Development
Provides: perl-IPC-System-Simple-devel = %{version}-%{release}

%description dev
dev components for the perl-IPC-System-Simple package.


%package license
Summary: license components for the perl-IPC-System-Simple package.
Group: Default

%description license
license components for the perl-IPC-System-Simple package.


%prep
%setup -q -n IPC-System-Simple-1.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IPC-System-Simple
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-IPC-System-Simple/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/IPC/System/Simple.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IPC::System::Simple.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IPC-System-Simple/LICENSE
