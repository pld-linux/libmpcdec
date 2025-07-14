#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Musepack SV7 decoding library
Summary(pl.UTF-8):	Biblioteka do dekodowania formatu musepack SV7
Name:		libmpcdec
Version:	1.2.6
Release:	4
License:	BSD
Group:		Libraries
#Source0Download: https://www.musepack.net/index.php?pg=src
Source0:	https://files.musepack.net/source/%{name}-%{version}.tar.bz2
# Source0-md5:	7f7a060e83b4278acf4b77d7a7b9d2c0
Patch0:		ac.patch
URL:		https://www.musepack.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
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

This library handles SV7 (StreamVersion7) format.

%description -l pl.UTF-8
Ta biblioteka obsługuje dekodowanie formatu MPC, który jest formatem
kompresji dźwięku z naciskiem na wysoką jakość. Nie jest bezstratny,
ale jest zaprojektowany dla przezroczystości tak, że nie można
usłyszeć różnicy między oryginalnym plikiem wave a dużo mniejszym
plikiem MPC. Jest oparty na algorytmach MPEG-1 Layer-2 / MP2, ale od
1997 roku został znacznie rozwinięty i ulepszony, a teraz jest w
zaawansowanym stadium, w którym zawiera silnie zoptymalizowany i nie
objęty patentami kod.

Ta biblioteka obsługuje format SV7 (StreamVersion7).

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
%patch -P0 -p1

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

cp -p src/sample.cpp $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libmpcdec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpcdec.so.5

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
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
