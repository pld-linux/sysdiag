%define	fver	%(echo %{version} | tr . _)
Summary:	Command line diagnostics
Summary(pl.UTF-8):	Narzędzie diagnostyczne działające z linii poleceń
Name:		sysdiag
Version:	0.3.0
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/linux-diag/%{name}-v%{fver}.tar.gz
# Source0-md5:	2906b73dfec0d962aa5e66aa3bb06088
Patch0:		%{name}-gcc33_fixes.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-system-libs.patch
URL:		http://linux-diag.sourceforge.net/Sysdiag.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	sysfsutils-devel >= 0.4.0
BuildRequires:	tdb-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sysdiag is a utility that enables the user to run diagnotics on
devices present on the system. It also enables the user to list all
the devices on the system, show event log information from the system
logs for the device. sysdiag makes use of libsysfs, which is a library
that provides set of APIs to query device information from the sysfs
undef Linux 2.5+.

%description -l pl.UTF-8
sysdiag to narzędzie pozwalające użytkownikowi na wykonanie
diagnostyki urządzeń obecnych w systemie. Pozwala także uzyskać listę
wszystkich urządzeń oraz wyświetlić informacje z logów systemowych o
zdarzeniach związanych z tym urządzeniem. sysdiag wykorzystuje
libsysfs - bibliotekę dostarczającą zbiór API do uzyskiwania
informacji o urządzeniach z sysfs pod Linuksem 2.5+.

%prep
%setup -q -n %{name}-v%{fver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export CPPFLAGS=-I/usr/include/sysfs
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--datadir=%{_sysconfdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs/sysdiag.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sysdiag.conf
%attr(755,root,root) %{_bindir}/sysdiag
%{_mandir}/man1/%{name}.1*
