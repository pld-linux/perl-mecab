#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires mecab dictionary)
#
Summary:	MeCab module for Perl
Summary(pl.UTF-8):	Moduł MeCab dla Perla
Name:		perl-mecab
Version:	0.996
Release:	14
License:	GPL v2 or LGPL v2.1 or BSD
Group:		Development/Languages/Perl
#Source0Download: http://code.google.com/p/mecab/downloads/list
Source0:	http://mecab.googlecode.com/files/mecab-perl-%{version}.tar.gz
# Source0-md5:	af03fd644dfdfa239c63ae6279bfc4ce
URL:		http://code.google.com/p/mecab/
BuildRequires:	libstdc++-devel
BuildRequires:	mecab-devel >= 0.996
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%{?with_tests:BuildRequires:	mecab-ipadic}
Requires:	mecab >= 0.996
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MeCab module for Perl.

%description -l pl.UTF-8
Moduł MeCab dla Perla.

%prep
%setup -q -n mecab-perl-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cxx}"
	OPTIMIZE="%{rpmcxxflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING README bindings.html
%{perl_vendorarch}/MeCab.pm
%dir %{perl_vendorarch}/auto/MeCab
%attr(755,root,root) %{perl_vendorarch}/auto/MeCab/MeCab.so
