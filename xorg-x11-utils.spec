%global debug_package %{nil}

Name:           xorg-x11-utils
Version:        7.5
Release:    	40%{dist}
Summary:        X.Org X11 X client utilities

License:        MIT
URL:            http://www.x.org
Source0:        https://www.x.org/releases/X11R7.7/doc/xorg-docs/README.txt


Requires:       xprop
Requires:	xdpyinfo
Requires:	xev
Requires:	xlsatoms
Requires:	xlsclients
Requires:	xlsfonts
Requires:	xprop
Requires:	xvinfo
Requires:	xwininfo

%description
A collection of client utilities which can be used to query the X server for
various information.

%prep
mkdir -p %{name}-%{version} 
mv -f %{S:0} %{name}-%{version}

%setup -T -D -n %{name}-%{version} 

%build
# None here


%install
# None here

%files 
%doc README.txt


%changelog

* Sun Oct 24 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 7.5-40  
- Initial build rpm
