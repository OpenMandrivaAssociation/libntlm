%define major 0
%define libname %mklibname ntlm %{major}
%define devname %mklibname ntlm -d

Summary:	Microsoft WinNT domain authentication library
Name:		libntlm
Version:	1.4
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.nongnu.org/libntlm/
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
%configure2_5x --disable-static
%make

%check
make check

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libntlm.so.%{major}*

%files -n %{devname}
%doc AUTHORS README ChangeLog THANKS
%{_includedir}/ntlm.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libntlm.pc

