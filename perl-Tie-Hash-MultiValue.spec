%define upstream_name    Tie-Hash-MultiValue
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Hash w/multiple items under a single key
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Simple)
BuildRequires: perl(Tie::Hash)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'Tie::Hash::MultiValue' allows you to have hashes which store their values
in anonymous arrays, appending any new value to the already-existing ones.

This means that you can store as many items as you like under a single key,
and access them all at once by accessing the value stored under the key.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*
