Summary:	Command line diagnostics
Summary(pl):	Narzêdzie diagnostyczne dzia³aj±ce z linii poleceñ
Name:		sysdiag
Version:	0.1.0
%define	fver	%(echo %{version} | tr . _)
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/linux-diag/%{name}-v%{fver}.tar.gz
# Source0-md5:	6f8ae797f4215647cee90a08607c332c
URL:		http://linux-diag.sourceforge.net/Sysdiag.html
#BuildRequires:	sysfsutils-devel = 0.1.0
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

%build
%configure

%{__make}
#	INCLUDES= \
#	LDADD=-lsysfs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs/sysdiag.txt
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sysdiag.conf
