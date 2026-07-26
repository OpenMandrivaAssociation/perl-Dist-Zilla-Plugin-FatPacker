%define upstream_name    Dist-Zilla-Plugin-FatPacker
Name:		perl-%{upstream_name}
Version:	1.161631
Release:	2

Summary:	Pack your dependencies onto your script file

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/doherty/Dist-Zilla-Plugin-FatPacker
Source0:	https://cpan.metacpan.org/authors/id/D/DO/DOHERTY/Dist-Zilla-Plugin-FatPacker-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires: perl(ok)
BuildRequires:	perl(App::FatPacker)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Dist::Zilla::Role::FileMunger)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This plugin uses the App::FatPacker manpage to pack your dependencies onto
your script file.

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
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%{perl_vendorlib}/*


