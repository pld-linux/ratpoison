Summary:	A simple X11 window manager
Summary(pl.UTF-8):	Prosty zarządca okien dla X11
Name:		ratpoison
Version:	1.4.5
Release:	4
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://savannah.nongnu.org/download/ratpoison/%{name}-%{version}.tar.gz
# Source0-md5:	330a08dbed6be88cab54f6947e9f0b60
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-getline.patch
URL:		http://www.nongnu.org/ratpoison/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	readline-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch0 -p1

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
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/*.texi
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/ratpoison.1*
%{_infodir}/*.info*
