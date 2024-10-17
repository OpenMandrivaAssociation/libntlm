%define major 0
%define libname %mklibname ntlm %{major}
%define devname %mklibname ntlm -d

Summary:	Microsoft WinNT domain authentication library
Name:		libntlm
Version:	1.6
Release:	2
Group:		System/Libraries
License:	LGPLv2+
Url:		https://www.nongnu.org/libntlm/
Source0:	http://www.nongnu.org/libntlm/releases/%{name}-%{version}.tar.gz
%ifnarch %arm %mips
BuildRequires:	valgrind
%endif

%description
A library for authenticating with Microsoft NTLM challenge-response, 
derived from Samba sources.

%package -n %{libname}
Summary:	Microsoft WinNT domain authentication library
Group:		System/Libraries

%description -n %{libname}
A library for authenticating with Microsoft NTLM challenge-response, 
derived from Samba sources.

%package -n %{devname}
Summary:	Microsoft WinNT domain authentication library for development
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files needed for compiling against libntlm.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%check
#make check

%install
%make_install

%files -n %{libname}
%{_libdir}/libntlm.so.%{major}*

%files -n %{devname}
%doc AUTHORS README ChangeLog THANKS
%{_includedir}/ntlm.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libntlm.pc

