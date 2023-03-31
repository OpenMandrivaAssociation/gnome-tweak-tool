%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	A tool to customize advanced GNOME 3 options
Name:		gnome-tweak-tool
Version:	3.27.3
Release:	4
Group:		Graphical desktop/GNOME
License:	GPLv3
Url:		http://live.gnome.org/GnomeTweakTool
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:  GConf2
BuildRequires:  meson
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  python-devel

Requires:	gnome-shell
Requires:	python-gi

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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
	--remove-only-show-in=Pantheon \
	%{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license LICENSES/*
%{_bindir}/%{name}
%{python3_sitelib}/gtweak/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/gnome-tweak-tool*.*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_libexecdir}/gnome-tweak-tool-lid-inhibitor

