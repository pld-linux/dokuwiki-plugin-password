%define		plugin		password
Summary:	DokuWiki plugin to hide passwords from plain view
Name:		dokuwiki-plugin-%{plugin}
Version:	20070926
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://rolandeckert.com/_media/projects/plugin-password.tgz
# Source0-md5:	cbbf05d46aced4b9d8586514ef367c64
URL:		http://www.dokuwiki.org/plugin:password
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20060309
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This password syntax plugin screens text from view. It may be used for
storing clear-text passwords which otherwise would be stored fully
visible. Only users with write access to the page can view the wiki
source. This may be just enough security for non-important passwords
or group access in an internal wiki.

%prep
%setup -qc
mv %{plugin}/* .

version=$(awk -F"'" '/date/{print $4}' syntax.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
