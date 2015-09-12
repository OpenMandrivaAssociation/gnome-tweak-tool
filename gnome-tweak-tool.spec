%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	A tool to customize advanced GNOME 3 options
Name:		gnome-tweak-tool
Version:	3.17.1
Release:	3
Group:		Graphical desktop/GNOME
License:	GPLv3
Url:		http://live.gnome.org/GnomeTweakTool
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)

Requires:	gnome-shell

%description
GNOME Tweak Tool is an application for changing the advanced settings
of GNOME 3.

Features:
* Install and switch gnome-shell themes
* Switch GTK+ themes
* Switch icon themes
* Change
  - The user-interface and title bar fonts
  - Icons in menus and buttons
  - Behavior on laptop lid close
  - Shell font size
  - File manager desktop icons
  - Title bar click action
  - Shell clock to show date
  - Font hinting
  - Font anti-aliasing

%prep
%setup -q
%apply_patches

%build
%configure \
	--build=%{_host}

%make

%install
%makeinstall_std
%find_lang %{name}

desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	--remove-only-show-in=Pantheon \
	%{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%{python_sitelib}/gtweak
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/*/*.png
%{_libexecdir}/gnome-tweak-tool-lid-inhibitor
%{_datadir}/appdata/gnome-tweak-tool.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/gnome-tweak-tool-symbolic.svg

