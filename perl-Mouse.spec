#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mouse
Summary:	Mouse - Moose minus the antlers
#Summary(pl.UTF-8):
Name:		perl-Mouse
Version:	0.50
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/CPAN/authors/id/G/GF/GFUJI/%{pdir}-%{version}.tar.gz
# Source0-md5:	529bd5241135c1dae8c382bb123bd586
URL:		http://search.cpan.org/dist/Mouse/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-Test-Exception >= 0.21
BuildRequires:	perl-Test-Simple >= 0.8
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moose is wonderful. Use Moose instead of Mouse.

Unfortunately, it's a little slow. Though significant progress has
been made over the years, the compile time penalty is a non-starter
for some applications.

Mouse aims to alleviate this by providing a subset of Moose's
functionality, faster. In particular, L<Moose/has> is missing only a
few expert-level features.

# %description -l pl.UTF-8

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
%{perl_vendorlib}/MouseX/
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/Mouse/
%{perl_vendorarch}/Squirrel/
%{perl_vendorarch}/Test/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/*.so
%{_mandir}/man3/*
