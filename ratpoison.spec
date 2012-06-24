Summary:	A simple X11 window manager
Summary(pl):	Prosty Window Manad�er dla X11
Name:		ratpoison
Version:	1.1.1
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://telia.dl.sourceforge.net/sourceforge/ratpoison/%{name}-%{version}.tar.gz
URL:		http://ratpoison.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define		_docdir		%{_prefix}/share/doc/%{name}

%description
ratpoison is a simple Window Manager with no fat library dependencies,
no fancy graphics, no window decorations, and no flashy wank. It is
largely modelled after GNU Screen which has done wonders in virtual
terminal market.

%description -l pl
Prosty Window Manad�er dla X11 zamodelowany na wz�r programu GNU
screen.

%prep
%setup -q -n %{name}-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/*
%doc %{_mandir}/man1/*
%doc %{_infodir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
