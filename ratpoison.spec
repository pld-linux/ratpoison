Summary:	A simple X11 window manager
Summary(pl.UTF-8):	Prosty zarządca okien dla X11
Name:		ratpoison
Version:	1.4.2
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4d055475b0678759cb78f6ba7ae9e86a
Source1:	%{name}-xsession.desktop
URL:		http://www.nongnu.org/ratpoison/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	readline-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_docdir		%{_prefix}/share/doc/%{name}

%description
ratpoison is a simple Window Manager with no fat library dependencies,
no fancy graphics, no window decorations, and no flashy wank. It is
largely modelled after GNU Screen which has done wonders in virtual
terminal market.

%description -l pl.UTF-8
ratpoison jest prostym zarządcą okien dla X11 pozbawionym zależności
od obszernych bibliotek, bez fantazyjnej grafiki i ozdobników okien.
Jest wzorowany na programie GNU screen, który wyczynia cuda w
dziedzinie terminali wirtualnych.

%prep
%setup -q

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

install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_docdir}
%doc %{_docdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*
%{_infodir}/*.info*
