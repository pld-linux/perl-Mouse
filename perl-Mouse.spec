#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Mouse
Summary:	Mouse - Moose minus the antlers
Name:		perl-Mouse
Version:	2.5.9
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/S/SK/SKAJI/%{pdir}-v%{version}.tar.gz
# Source0-md5:	ffc0f03b781a70a585097a97fe107d9f
URL:		http://search.cpan.org/dist/Mouse/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build-XSUtil
%if %{with tests}
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-Test-Exception >= 0.21
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.8
BuildRequires:	perl-Test-LeakTrace
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

%prep
%setup -q -n %{pdir}-v%{version}

%build
%{__perl} Build.PL \
        destdir=$RPM_BUILD_ROOT \
	installdirs=vendor

./Build \
	CFLAGS="%{rpmcflags}"

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/MouseX

./Build install

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
