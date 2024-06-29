#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	Mouse
Summary:	Mouse - Moose minus the antlers
Summary(pl.UTF-8):	Mouse - Moose minus poroże
Name:		perl-Mouse
Version:	2.5.10
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SK/SKAJI/%{pdir}-v%{version}.tar.gz
# Source0-md5:	0dd19d703e14af71d723ba787d631858
URL:		https://metacpan.org/dist/Mouse
BuildRequires:	perl-Devel-PPPort >= 3.42
BuildRequires:	perl-ExtUtils-ParseXS >= 3.22
BuildRequires:	perl-Module-Build >= 0.4005
BuildRequires:	perl-Module-Build-XSUtil >= 0.19
BuildRequires:	perl-devel >= 1:5.8.5
BuildRequires:	perl-version >= 0.9913
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(XSLoader) >= 0.02
BuildRequires:	perl-Scalar-List-Utils >= 1.14
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-LeakTrace
BuildRequires:	perl-Test-Output
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Try-Tiny
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moose is wonderful. Use Moose instead of Mouse.

Unfortunately, it's a little slow. Though significant progress has
been made over the years, the compile time penalty is a non-starter
for some applications.

Mouse aims to alleviate this by providing a subset of Moose's
functionality, faster. In particular, Moose/has is missing only a
few expert-level features.

%description -l pl.UTF-8
Moose jest cudowny. Lepiej używać Moose zamiast Mouse.

Niestety, Moose jest nieco wolny. Mimo znaczących postępów w ostatnich
latach, wzrost czasu kompilacji jest nieakceptowalny w niektórych
zastosowaniach.

Celem Mouse jest złagodzenie tej wady poprzez dostarczenie podzbioru
funkcjonalności Moose, działającego szybciej. W szczególności
Moose/has brakuje tylko kilku funkcji używanych przez ekspertów.

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Mouse/Mouse.bs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/MouseX
%{perl_vendorarch}/Mouse.pm
%{perl_vendorarch}/Mouse
%{perl_vendorarch}/Squirrel.pm
%{perl_vendorarch}/Squirrel
%{perl_vendorarch}/Test/Mouse.pm
%{perl_vendorarch}/ouse.pm
%dir %{perl_vendorarch}/auto/Mouse
%attr(755,root,root) %{perl_vendorarch}/auto/Mouse/Mouse.so
%{_mandir}/man3/Mouse.3pm*
%{_mandir}/man3/Mouse::*.3pm*
%{_mandir}/man3/Squirrel*.3pm*
%{_mandir}/man3/Test::Mouse.3pm*
%{_mandir}/man3/ouse.3pm*
