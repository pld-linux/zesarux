#
# Conditional build:
#
Summary:	ZX Second-Emulator And Released for UniX
Name:		zesarux
Version:	5.0
Release:	1
License:	GPL v3+
Group:		Applications/Emulators
Source0:	http://downloads.sourceforge.net/zesarux/ZEsarUX_src-%{version}.tar.gz
# Source0-md5:	438004aac06df5b70eab4496e031252d
Patch0:		DESTDIR.patch
URL:		http://zesarux.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	aalib-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	libcaca-devel
BuildRequires:	libsndfile-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZEsarUX - ZX Second-Emulator And Released for UniX

It's a ZX Machines Emulator for Unix, including:

- -ZX80
- -ZX81
- -ZX Spectrum
- -QL
- -Z88
- -Timex TS 2068
- -Sam Coupe
- -Pentagon 128
- -Chloe 140 SE, Chloe 280 SE
- -ZX-Uno
- -Prism
- -TBBlue/ZX Spectrum Next
- -Jupiter Ace
- -Amstrad CPC 464

%prep
%setup -q -n ZEsarUX-%{version}
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" ./configure \
	--prefix %{_prefix} \
	--enable-memptr \
	--enable-visualmem \
	--enable-cpustats
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT{ACKNOWLEDGEMENTS,ALTERNATEROMS,Changelog,FAQ,FEATURES,HISTORY,INCLUDEDTAPES,INSTALL,INSTALLWINDOWS,LICENSE,LICENSE_MOTOROLA_CORE,README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS ALTERNATEROMS Changelog FAQ FEATURES HISTORY INCLUDEDTAPES INSTALL INSTALLWINDOWS LICENSE LICENSE_MOTOROLA_CORE README
%attr(755,root,root) %{_bindir}/zesarux
%{_datadir}/zesarux
