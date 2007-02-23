Name:           wxkeyring
Version:        0.94
Release:        1%{?dist}
Summary:        Fetch info from GNU Keyring files

Group:          Applications/Productivity
License:        Artistic
URL:            http://johan.vromans.org/software/sw_palmkeyring.html
Source0:        wxkeyring-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Requires:	perl-Palm-Keyring >= 0.93
Requires:	perl-Wx >= 0.67

%description
wxkeyring provides a (currently read-only) interface to the
keyring files as used by the GNU KeyRing tool on Palm handhelds.

%prep
%setup -q

%build
# Remove OPTIMIZE=... from noarch packages (unneeded)
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README wxkeyring.wxg
# For noarch packages: vendorlib
# %{perl_vendorlib}/*
# For arch-specific packages: vendorarch
# %{perl_vendorarch}/auto/*
# %{perl_vendorarch}/everything-except-"auto"
%{_mandir}/man1/*.1*
%{_bindir}/wxkeyring

%changelog
