
%define		_splash		MoonKDE

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	0.2
Release:	2
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=7289&id=1
Source0:	http://www.kde-look.org/content/files/7289-MoonKDE-%{version}.tar.bz2
# Source0-md5:	0d2cd77284bd7b3968294ee408b0560d
URL:		http://www.kde-look.org/content/show.php?content=7289
Provides:	kde-splash
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Full moon over some mysterious lake. Very nice piece of graphics :)

%description -l pl
Pe³nia ksiê¿yca nad brzegiem tajemniczego jeziorka. Bardzo ³adny
kawa³ek grafiki :)

%prep
%setup -q -n %{_splash}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
