Summary:	libicq2000 library
Summary(pl):	Biblioteka libicq2000
Name:		libicq2000
Version:	0.3.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://telia.dl.sourceforge.net/sourceforge/libicq2000/%{name}-%{version}.tar.gz
URL:		http://libicq2000.sf.net/
BuildRequires:	libsigc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libicq2000 is an opensource C++ library being developed to support the
icq2000/2001 protocol. It is easy for developers to use as the
backbone for their clients' connection to the ICQ network - all the
protocol work is abstracted away in one nice object-orientated
interface.

%package devel
Summary:	Header files etc to develop libicq2000 applications
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files etc you can use to develop libicq2000 applications.

%package static
Summary:	Static libicq2000 libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libicq2000 libraries.

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%doc doc/html
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/libicq2000
%{_aclocaldir}/*.m4
%{_mandir}/man1/*-config*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
