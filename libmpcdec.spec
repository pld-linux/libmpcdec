Summary:	Musepack decoding library
Summary(pl):	Biblioteka do dekodowania formatu musepack
Name:		libmpcdec
Version:	1.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://musepack.origean.net/files/source/%{name}-%{version}.tar.bz2
# Source0-md5:	f8465cc807c4d8acca6da250fd4ca9b0
URL:		http://www.musepack.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
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

%description -l pl
Ta biblioteka obs�uguje dekodowanie formatu MPC, kt�ry jest formatem
kompresji d�wi�ku z naciskiem na wysok� jako��. Nie jest bezstratny,
ale jest zaprojektowany dla przezroczysto�ci, tak, �e nie mo�na
us�ysze� r�nicy mi�dzy oryginalnym plikiem wave a du�o mniejszym
plikiem MPC. Jest oparty na algorytmach MPEG-1 Layer-2 / MP2, ale od
1997 roku zosta� znacznie rozwini�ty i ulepszony, a teraz jest w
zaawansowanym stadium, w kt�rym zawiera silnie zoptymalizowany i nie
obj�ty patentami kod.

%package devel
Summary:	Header files for libmpcdec
Summary(pl):	Pliki nag��wkowe do biblioteki libmpcdec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmpcdec.

%description devel -l pl
Pliki nag��wkowe do biblioteki libmpcdec.

%package static
Summary:	Static version of the libmpcdec library
Summary(pl):	Statyczna wersja biblioteki libmpcdec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of the libmpcdec library.

%description static -l pl
Statyczna wersja biblioteki libmpcdec.

%package examples
Summary:	Example of using libmpcdec with documentation
Summary(pl):	Przyk�ad u�ycia libmpcdec z dokumentacj�
Group:		Documentation

%description examples
Example of using libmpcdec with documentation.

%description examples -l pl
Przyk�ad u�ycia libmpcdec z dokumentacj�.

%prep
%setup -q

%build
%{?debug:%{__sed} -i -e "s,-O3 -fomit-frame-pointer,,g" configure.ac}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libmpcdec.a

%files examples
%doc docs/html
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
