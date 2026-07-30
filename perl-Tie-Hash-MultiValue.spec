%define upstream_name    Tie-Hash-MultiValue
%define upstream_version 1.07
Name:		perl-%{upstream_name}
Version:	1.07
Release:	1

Summary:	Hash w/multiple items under a single key
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Tie-Hash-MultiValue
Source0:	https://cpan.metacpan.org/authors/id/M/MC/MCMAHON/Tie-Hash-MultiValue-1.07.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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


