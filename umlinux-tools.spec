Summary:	User Mode Linux tools
Summary(pl.UTF-8):	Narzędzia dla Linuksa w przestrzeni użytkownika
Name:		umlinux-tools
Version:	20070815
Release:	6
License:	GPL v2
Group:		Applications/Emulators
Source0:	http://user-mode-linux.sourceforge.net/uml_utilities_%{version}.tar.bz2
# Source0-md5:	b0468ac8b79cef53f36f5f9517907462
Patch0:		%{name}-Makefile.patch
Patch1:		no-hardcoded-libdir.patch
Patch2:		build.patch
URL:		http://user-mode-linux.sourceforge.net/
BuildRequires:	libfuse-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User Mode Linux tools.

%description -l pl.UTF-8
Narzędzia dla Linuksa w przestrzeni użytkownika.

%prep
%setup -q -n tools-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall" \
	LDFLAGS="%{rpmldflags}" \
	LIB_DIR=%{_libdir}/uml

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIB_DIR=%{_libdir}/uml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/jail_uml
%dir %{_libdir}/uml
%attr(755,root,root) %{_libdir}/uml/port-helper
%doc Changelog
