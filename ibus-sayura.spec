Name:       ibus-sayura
Version:    1.3.2
Release:    3%{?dist}
Summary:    The Sinhala engine for IBus input platform
License:    GPLv2+
Group:      System Environment/Libraries
URL:        https://fedorahosted.org/ibus-sayura
Source0:    https://fedorahosted.org/releases/i/b/ibus-sayura/%{name}-%{version}.tar.gz

BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  ibus-devel
Requires:   ibus
%description
The Sayura engine for IBus platform. It provides Sinhala input method.

%prep
%setup -q

%build
%configure --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-sayura
%{_datadir}/ibus-sayura
%{_datadir}/ibus/component/*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.3.2-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.3.2-2
- Mass rebuild 2013-12-27

* Wed Mar 27 2013 Pravin Satpute <psatpute@redhat.com> - 1.3.2-1
- configured with autoconf-2.69

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Pravin Satpute <psatpute@redhat.com> - 1.3.1-6
- spec file clean up

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Pravin Satpute <psatpute@redhat.com> - 1.3.1-4
- rebuild for broken dependancies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 26 2011 Pravin Satpute <psatpute@redhat.com> - 1.3.1-2
- Resolved bug #741176

* Thu Feb 24 2011 Pravin Satpute <psatpute@redhat.com> - 1.3.1-1
- upstream release 1.3.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0.20100716-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 26 2010 Pravin Satpute <psatpute@redhat.com> - 1.3.0.20100716-3
- adding rank to ibus-sayura

* Mon Nov 08 2010 Pravin Satpute <psatpute@redhat.com> - 1.3.0.20100716-2
- rebuild for broken dependancies

* Fri Jul 16 2010 Pravin Satpute <psatpute@redhat.com> - 1.3.0.20100716-1
- upstream new release

* Tue Jun 15 2010 Pravin Satpute <psatpute@redhat.com> - 1.2.99.20100209-2
- fixed bug 601568

* Tue Feb 09 2010 Pravin Satpute <pravin.d.s@gmail.com> - 1.2.99.20100209-1
- updated patches for code enhancements from phuang for ibus-1.2.99

* Mon Feb 08 2010 Adam Jackson <ajax@redhat.com> 1.2.0.20090703-4
- Rebuild for new libibus.so.2 ABI

* Tue Nov 17 2009 Pravin Satpute <psatpute@redhat.com> - @VERSON@-3
- fixed bug 528405

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090703-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Pravin Satpute <psatpute@redhat.com> - @VERSON@-1
- upstream release 1.2.0

* Mon Jun 29 2009 Pravin Satpute <pravin.d.s@gmail.com> - @VERSON@-4
- fix for bug 507209

* Mon Jun 29 2009 Parag <panemade@gmail.com> - 1.0.0.20090326-3
- Rebuild against newer ibus

* Thu Mar 26 2009 Pravin Satpute <pravin.d.s@gmail.com> - @VERSON@-2
- updated as per fedora spec review

* Fri Mar 20 2009 Pravin Satpute <pravin.d.s@gmail.com> - 1.0.0.20090326-1
- The first version.
