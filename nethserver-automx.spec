Summary: NethServer configuration for automx
%define name nethserver-automx
%define version 0.0.1
%define release 6
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: https://github.com/danb35/nethserver-automx

BuildRequires: nethserver-devtools
Requires: automx
Requires: nethserver-httpd
Requires: python-ldap
#AutoReq: no

%description
NethServer configuration for automx (https://automx.org)

%prep
%setup

%post
mkdir -p /var/log/automx
chown apache:apache /var/log/automx

%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} %{buildroot} $RPM_BUILD_ROOT > default.lst

%clean
rm -rf $RPM_BUILD_ROOT

%files -f default.lst
%dir %{_nseventsdir}/%{name}-update

%changelog
* Sat Sep  8 2018 Dan Brown <dan@familybrown.org> - 0.0.1-6.ns7
- Added dependency on python-ldap
- Created and set ownership of log directory

* Sun Aug 26 2018 Dan Brown <dan@familybrown.org> - 0.0.1-5.ns7
- Changed virtual host configuration to correct Let's Encrypt renewal

* Fri Jun 15 2018 Dan Brown <dan@familybrown.org> - 0.0.1-4.el7
- Update 05autoconfig_vhost template to include document root for automx-web

* Wed Jun 13 2018 Dan Brown <dan@familybrown.org> - 0.0.1-3.el7
- Updated createlinks script to expand templates and restart services properly

* Fri Jun  8 2018 dan@familybrown.org - 0.0.1-2
- Added virtualhost template fragment
- Added config option to sign mobileconfig files
- Removed dependency on automx-web
- Added dependency on nethserver-httpd
* Tue Oct 24 2017 Stefano Zamboni <s.zamboni@dataveneta.it> - 0.0.1-ns7
- Initial release
