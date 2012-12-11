%define upstream_name    Tie-Hash-MultiValue
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Hash w/multiple items under a single key
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(Tie::Hash)

BuildArch:	noarch

%description
'Tie::Hash::MultiValue' allows you to have hashes which store their values
in anonymous arrays, appending any new value to the already-existing ones.

This means that you can store as many items as you like under a single key,
and access them all at once by accessing the value stored under the key.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 655238
- rebuild for updated spec-helper

* Thu Dec 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 479670
- removing old tarball

* Thu Dec 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.1
+ Revision: 479669
- update to 1.02

* Sun Dec 13 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.1
+ Revision: 478062
- update to 1.01

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 466795
- import perl-Tie-Hash-MultiValue


* Tue Nov 17 2009 cpan2dist 0.06-1mdv
- initial mdv release, generated with cpan2dist
