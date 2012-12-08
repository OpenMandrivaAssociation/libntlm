%define major 0
%define libname %mklibname ntlm %{major}
%define develname %mklibname ntlm -d

Summary:	Microsoft WinNT domain authentication library
Name:		libntlm
Version:	1.3
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.nongnu.org/libntlm/
Source0:	http://www.nongnu.org/libntlm/releases/%{name}-%{version}.tar.gz
%ifnarch %arm %mips
BuildRequires:	valgrind
%endif
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
%{_libdir}/pkgconfig/libntlm.pc


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2-3mdv2011.0
+ Revision: 661507
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2-2mdv2011.0
+ Revision: 602586
- rebuild

* Sun Jan 24 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2-1mdv2010.1
+ Revision: 495551
- update to new version 1.2

* Sun Sep 27 2009 Olivier Blin <oblin@mandriva.com> 1.1-2mdv2010.0
+ Revision: 449907
- do not use valgrind on mips & arm (from Arnaud Patard)

* Sat May 09 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1-1mdv2010.0
+ Revision: 373874
- update to new version 1.1

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2009.0
+ Revision: 264850
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 27 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-1mdv2009.0
+ Revision: 211987
- add source and spec file
- Created package structure for libntlm.

