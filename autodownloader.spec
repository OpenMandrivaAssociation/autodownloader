Name:           autodownloader
Version:        0.3.0
Release:        1
Summary:        GUI-tool to automate the download of certain files
License:        GPLv2+
Group:          Networking/File transfer 
URL:            http://sourceforge.net/projects/autodownloader
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       pygtk2.0-libglade hicolor-icon-theme

%description
Some software (usually games) requires certain data files to operate, sometimes
these datafiles can be freely downloaded but may not be redistributed and thus
cannot be put into so called packages as part of a distro.

autodownloader is a tool which can be used as part of a package to automate the
download of the needed files. It will prompt the user explaining to him the
need of the download and asking if it is ok to make an internet connection,
after this it will show the license of the to be downloaded files and last it
will do the actual download and md5 verification off these files. This whole
process can be configured by the packager through a simple configuration file.

Notice that Autodownloader while open source itself, may download files which
are not permitted to be (re)distributed unlike most files in Fedora.

%files
%doc COPYING ChangeLog GladeWindow-license.txt README.txt TODO example.autodlrc
%{_datadir}/autodl
%{_datadir}/icons/hicolor/*/apps/autodl.png

#--------------------------------------------------------------------

%prep
%setup -q
# python3
find . -name "*.py" -exec 2to3 -w {} \;

%build
# nothing to build pure python code only

%install
%makeinstall_std