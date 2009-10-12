# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name: sugar-fructose
Version: 0.86.2
Release: %mkrel 1
Summary: Core Sugar activities
License: GPL/LGPL
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Requires: sugar-calculate-activity >= 30
Requires: sugar-chat-activity >= 66
Requires: sugar-etoys-activity >= 109
Requires: sugar-imageviewer-activity >= 14
Requires: sugar-jukebox-activity >= 11
Requires: sugar-log-activity >= 23
Requires: sugar-pippy-activity >= 34
Requires: sugar-read-activity >= 76
Requires: sugar-toolkit >= 0.86.1
Requires: sugar-terminal-activity >= 28
Requires: sugar-turtleart-activity >= 73
Requires: sugar-browse-activity >= 114
Requires: sugar-write-activity >= 68

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This virtual package depends on core Sugar activities that follow the Sugarlabs
six months release schedule.
Sugar is a graphical user interface aimed at children which promotes sharing
and collaborative learning. It was introduced on the One Laptop Per Child
(OLPC) XO laptop but is useful on other devices as well.

%files
%defattr(-,root,root,-)

