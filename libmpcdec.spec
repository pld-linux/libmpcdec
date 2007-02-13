#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Musepack decoding library
Summary(pl.UTF-8):	Biblioteka do dekodowania formatu musepack
Name:		libmpcdec
Version:	1.2.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://files2.musepack.net/source/%{name}-%{version}.tar.bz2
# Source0-md5:	f14e07285b9b102a806649074c1d779b
URL:		http://www.musepack.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
Obsoletes:	libmusepack
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library handles decoding of the MPC format, which is an audio
compression format with a strong emphasis on high quality. It's not
lossless, but it is designed for transparency, so that you won't be
able to hear differences between the original wave file and the much
smaller MPC file. It is based on the MPEG-1 Layer-2 / MP2 algorithms,
but since 1997 it has rapidly developed and vastly improved and is now
at an advanced stage in which it contains heavily optimized and
patentless code.

%description -l pl.UTF-8
Ta biblioteka obsługuje dekodowanie formatu MPC, który jest formatem
kompresji dźwięku z naciskiem na wysoką jakość. Nie jest bezstratny,
ale jest zaprojektowany dla przezroczystości tak, że nie można
usłyszeć różnicy między oryginalnym plikiem wave a dużo mniejszym
plikiem MPC. Jest oparty na algorytmach MPEG-1 Layer-2 / MP2, ale od
1997 roku został znacznie rozwinięty i ulepszony, a teraz jest w
zaawansowanym stadium, w którym zawiera silnie zoptymalizowany i nie
objęty patentami kod.

%package devel
Summary:	Header files for libmpcdec
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki libmpcdec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libmusepack-devel

%description devel
Header files for libmpcdec.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki libmpcdec.

%package static
Summary:	Static version of the libmpcdec library
Summary(pl.UTF-8):	Statyczna wersja biblioteki libmpcdec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libmusepack-static

%description static
Static version of the libmpcdec library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libmpcdec.

%package examples
Summary:	Example of using libmpcdec with documentation
Summary(pl.UTF-8):	Przykład użycia libmpcdec z dokumentacją
Group:		Documentation

%description examples
Example of using libmpcdec with documentation.

%description examples -l pl.UTF-8
Przykład użycia libmpcdec z dokumentacją.

%prep
%setup -q

%build
%{?debug:%{__sed} -i -e "s,-O3 -fomit-frame-pointer,,g" configure.ac}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/sample.cpp $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libmpcdec.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpcdec.so
%{_libdir}/libmpcdec.la
%{_includedir}/mpcdec

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmpcdec.a
%endif

%files examples
%doc docs/html
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
