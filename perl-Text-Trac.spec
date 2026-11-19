#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Text
%define		pnam	Trac
Summary:	Text::Trac - extension for formatting text with Trac Wiki Style
Name:		perl-Text-Trac
Version:	0.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/M/MA/MANWAR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e241d0ee3a9b2e9b6360de97e15adbd5
URL:		http://search.cpan.org/dist/Text-Trac/
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Class-Data-Inheritable
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Path-Tiny
BuildRequires:	perl-Test-Base
BuildRequires:	perl-Tie-IxHash
BuildRequires:	perl-UNIVERSAL-require
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Trac parses text with Trac WikiFormatting and convert it to html
format.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__sed} -i -e '1s,^#!.*/env perl,#!%{__perl},' script/trac2html

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%attr(755,root,root) %{_bindir}/trac2html
%{perl_vendorlib}/Text/Trac.pm
%{perl_vendorlib}/Text/Trac
%{_mandir}/man3/*
