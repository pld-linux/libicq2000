Summary:	libicq2000 library
Summary(pl.UTF-8):	Biblioteka libicq2000
Name:		libicq2000
Version:	0.3.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libicq2000/%{name}-%{version}.tar.gz
# Source0-md5:	bab0e61b540258e54eb1c3695ac75f6e
URL:		http://libicq2000.sourceforge.net/
BuildRequires:	automake
BuildRequires:	libsigc++1-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libicq2000 is an opensource C++ library being developed to support the
icq2000/2001 protocol. It is easy for developers to use as the
backbone for their clients' connection to the ICQ network - all the
protocol work is abstracted away in one nice object-orientated
interface.

%description -l pl.UTF-8
libicq2000 to biblioteka C++ z otwartym kodem, tworzona do obsługi
protokołu icq2000/2001. Jest łatwa w użyciu dla programistów jako
obsługa połączenia do sieci ICQ dla klientów - całość obsługi
protokołu jest wyodrębniona do obiektowo zorientowanego interfejsu.

%package devel
Summary:	Header files etc to develop libicq2000 applications
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji libicq2000
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc you can use to develop libicq2000 applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe służące do tworzenia aplikacji opartych na
libicq2000.

%package static
Summary:	Static libicq2000 libraries
Summary(pl.UTF-8):	Statyczne biblioteki libicq2000
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libicq2000 libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libicq2000.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libicq2000
%{_aclocaldir}/*.m4
%{_mandir}/man1/*-config*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
