%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	A tool to customize advanced GNOME 3 options
Name:		gnome-tweak-tool
Version:	3.6.1
Release:	3
Group:		Graphical desktop/GNOME
License:	GPLv3
Url:		http://live.gnome.org/GnomeTweakTool
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch1:		gnome-tweak-tool-3.6.1-remove_lid_close_settings.patch
BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	GConf2
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(pygobject-3.0)

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
%configure2_5x \
	--build=%{_host}

%make

%install
%makeinstall_std
%find_lang %{name}

desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	--remove-only-show-in=Unity \
	%{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%{python_sitelib}/gtweak
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/*/*.png

