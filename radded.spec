Summary:	Stupid addon for LiCe
Summary(pl):	G�upi dodatek do LiCe
Summary(de):	Dumm der Zusat f�r LiCe
Name:		radded
Version:	1.5pre2
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://www.baseciq.org/radded/radded/%{name}-%{version}.tar.gz
URL:		http://www.baseciq.org/radded/
Requires:	lice
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
radded! is an Epic/LiCe addon, bringing you the most useful features
from other LiCe addons like wolf or VoiD.

%description -l de
radded! ist der Zusatz f�r Epic/LiCe, verbindend die Zunften am
interessansten anderes die Zusatzen z.B. Wolf oder VoiD

%description -l pl
radded! jest dodatkiem do Epic/LiCe, ��cz�cym najciekawsze cechy
innych dodatk�w takich jak wolf czy VoiD.

%prep
%setup -q -a 0 -n .irc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/epic/script/themes/

install *.reasons *.scr $RPM_BUILD_ROOT%{_datadir}/epic/script/
install themes/* $RPM_BUILD_ROOT%{_datadir}/epic/script/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc radded.readme.txt
%{_datadir}/epic/script/*.scr
%{_datadir}/epic/script/*.reasons
%{_datadir}/epic/script/themes/*
