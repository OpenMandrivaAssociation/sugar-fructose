# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-fructose
Version: 0.83.3
Release: %mkrel 1
Summary: Core Sugar activities
License: GPL/LGPL
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Requires: sugar-toolkit >= 0.83.3
Requires: sugar-browse-activity >= 102
Requires: sugar-turtleart-activity >= 23
Requires: sugar-imageviewer-activity >= 5
Requires: sugar-terminal-activity >= 21
Requires: sugar-etoys-activity >= 4.0.2201
Requires: sugar-calculate-activity >= 26
Requires: sugar-log-activity >= 16
Requires: sugar-chat-activity >= 61
Requires: sugar-write-activity >= 60
Requires: sugar-read-activity >= 62
Requires: sugar-jukebox-activity >= 6
Requires: sugar-pippy-activity >= 25

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This virtual package depends on core Sugar activities that follow the Sugarlabs
six months release schedule.
Sugar is a graphical user interface aimed at children which promotes sharing
and collaborative learning. It was introduced on the One Laptop Per Child
(OLPC) XO laptop but is useful on other devices as well.

%files
%defattr(-,root,root,-)

