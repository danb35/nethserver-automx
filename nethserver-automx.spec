Summary: NethServer configuration for automx
%define name nethserver-automx
%define version 0.0.1
%define release 5
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools
Requires: automx nethserver-httpd
#AutoReq: no

%description
NethServer configuration for automx (https://automx.org)

%prep
%setup

%post
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
* Sun Aug 26 2018 Dan Brown <dan@familybrown.org> - 0.0.1-5.el7
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
