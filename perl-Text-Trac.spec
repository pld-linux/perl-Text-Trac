#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Text
%define		pnam	Trac
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Trac - extension for formatting text with Trac Wiki Style
Name:		perl-Text-Trac
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	57757c5e9c742232b811af33b224357a
URL:		http://search.cpan.org/dist/Text-Trac/
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Base
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Trac parses text with Trac WikiFormatting and convert it to html
format.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc README
%{perl_vendorlib}/Text/Trac.pm
%{perl_vendorlib}/Text/Trac
%{_mandir}/man3/*
