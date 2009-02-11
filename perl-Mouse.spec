#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mouse
Summary:	Mouse - Moose minus the antlers
#Summary(pl.UTF-8):	
Name:		perl-Mouse
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SA/SARTAK/%{pdir}-%{version}.tar.gz
# Source0-md5:	90f0fb90430d245d68a6cee3c8e21c9a
URL:		http://search.cpan.org/dist/Mouse/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::Method::Modifiers) >= 1.01
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
L<Moose> is wonderful.

Unfortunately, it's a little slow. Though significant progress has
been made over the years, the compile time penalty is a non-starter
for some applications.

Mouse aims to alleviate this by providing a subset of Moose's
functionality, faster. In particular, L<Moose/has> is missing only
a few expert-level features.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/MouseX

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Mouse/
%{perl_vendorlib}/MouseX/
%{perl_vendorlib}/Squirrel/
%{_mandir}/man3/*
