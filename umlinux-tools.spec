# TODO: optflags
Summary:	User Mode Linux tools
Summary(pl.UTF-8):   Narzędzia dla Linuksa w przestrzeni użytkownika
Name:		umlinux-tools
Version:	20060323
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.user-mode-linux.org/~blaisorblade/uml-utilities/uml_utilities_%{version}.tar.bz2
# Source0-md5:	2d6678c939093a8212f994005a393508
URL:		http://user-mode-linux.sourceforge.net/
BuildRequires:	libpcap-static
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User Mode Linux tools.

%description -l pl.UTF-8
Narzędzia dla Linuksa w przestrzeni użytkownika.

%prep
%setup -q -n tools-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%dir %{_libdir}/uml
%attr(755,root,root) %{_libdir}/uml/port-helper
