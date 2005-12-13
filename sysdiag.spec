Summary:	Command line diagnostics
Summary(pl):	Narzêdzie diagnostyczne dzia³aj±ce z linii poleceñ
Name:		sysdiag
Version:	0.3.0
%define	fver	%(echo %{version} | tr . _)
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

%define		_datadir	%{_sysconfdir}

%description
sysdiag is a utility that enables the user to run diagnotics on
devices present on the system. It also enables the user to list all
the devices on the system, show event log information from the system
logs for the device. sysdiag makes use of libsysfs, which is a library
that provides set of APIs to query device information from the sysfs
undef Linux 2.5+.

%description -l pl
sysdiag to narzêdzie pozwalaj±ce u¿ytkownikowi na wykonanie
diagnostyki urz±dzeñ obecnych w systemie. Pozwala tak¿e uzyskaæ listê
wszystkich urz±dzeñ oraz wy¶wietliæ informacje z logów systemowych o
zdarzeniach zwi±zanych z tym urz±dzeniem. sysdiag wykorzystuje
libsysfs - bibliotekê dostarczaj±c± zbiór API do uzyskiwania
informacji o urz±dzeniach z sysfs pod Linuksem 2.5+.

%prep
%setup -q -n %{name}-v%{fver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

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
