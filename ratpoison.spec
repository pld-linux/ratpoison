Summary:	A simple X11 window manager
Summary(pl):	Prosty zarz±dca okien dla X11
Name:		ratpoison
Version:	1.2.2
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7cc7a1149554b2f76e4c52d5c3592b74
Source1:        %{name}-xsession.desktop
URL:		http://ratpoison.sourceforge.net/
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/*
%doc %{_mandir}/man1/*
%doc %{_infodir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
