Summary:	A simple X11 window manager
Summary(pl):	Prosty zarz±dca okien dla X11
Name:		ratpoison
Version:	1.3.0
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	75541248c355a3f1e09e864dd23a43f4
Source1:	%{name}-xsession.desktop
URL:		http://ratpoison.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_docdir		%{_prefix}/share/doc/%{name}

%description
ratpoison is a simple Window Manager with no fat library dependencies,
no fancy graphics, no window decorations, and no flashy wank. It is
largely modelled after GNU Screen which has done wonders in virtual
terminal market.

%description -l pl
ratpoison jest prostym zarz±dc± okien dla X11 pozbawionym zale¿no¶ci
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_docdir}/
%doc %{_docdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*
%{_infodir}/*.info*
