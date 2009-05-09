%define major 0
%define libname %mklibname ntlm %{major}
%define develname %mklibname ntlm -d

Summary:	Microsoft WinNT domain authentication library
Name:		libntlm
Version:	1.1
Release:	%mkrel 1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://josefsson.org/libntlm/
Source0:	http://josefsson.org/libntlm/releases/%{name}-%{version}.tar.gz
BuildRequires:	valgrind
BuildRoot:	%{_tmppath}/root-%{name}-%{version}

%description
A library for authenticating with Microsoft NTLM challenge-response, 
derived from Samba sources.

%package -n %{libname}
Summary:	Microsoft WinNT domain authentication library
Group:		System/Libraries

%description -n %{libname}
A library for authenticating with Microsoft NTLM challenge-response, 
derived from Samba sources.

%package -n %{develname}
Summary:	Microsoft WinNT domain authentication library for development
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files needed for compiling against libntlm.

%prep
%setup -q

%build
%configure2_5x
%make

%check
make check

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog THANKS
%{_includedir}/ntlm.h
%{_libdir}/*.so
%{_libdir}/libntlm.a
%{_libdir}/libntlm.la
%{_libdir}/pkgconfig/libntlm.pc
