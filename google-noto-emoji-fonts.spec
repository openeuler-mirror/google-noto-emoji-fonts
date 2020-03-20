Name:               google-noto-emoji-fonts
Version:            20180814
Release:            4
Summary:            Color and Black-and-White noto emoji fonts

License:            OFL and ASL 2.0
URL:                https://github.com/googlei18n/noto-emoji
Source0:            https://github.com/googlefonts/noto-emoji/archive/v2018-08-10-unicode11.tar.gz
Source1:            google-noto-emoji.metainfo.xml
Source2:            google-noto-emoji-color.metainfo.xml

Patch0:             noto-emoji-use-system-pngquant.patch
Patch1:             noto-emoji-build-all-flags.patch
Patch2:             noto-emoji-use-gm.patch
Patch3:             noto-emoji-python2.patch

BuildArch:          noarch

BuildRequires:      fontpackages-devel fonttools python2-fonttools nototools python2-devel
BuildRequires:      GraphicsMagick pngquant zopfli cairo-devel python2-nototools gdb

Requires:           fontpackages-filesystem

Provides:           google-noto-color-emoji-fonts = 20150617 google-noto-emoji-color-fonts
Obsoletes:          google-noto-color-emoji-fonts < 20150617 google-noto-emoji-color-fonts

%description
This package includes color and Black-and-White noto emoji fonts, and tools for working with them.

%_font_pkg NotoEmoji-Regular.ttf NotoColorEmoji.ttf
%license LICENSE
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md

%{_datadir}/appdata/google-noto-emoji.metainfo.xml
%{_datadir}/appdata/google-noto-emoji-color.metainfo.xml

%prep
%autosetup -n noto-emoji-2018-08-10-unicode11

rm -rf third_party/pngquant

%build

%install
install -m 0755 -d %{buildroot}/usr/share/fonts/google-noto-emoji
install -m 0644 -p fonts/NotoColorEmoji.ttf %{buildroot}/usr/share/fonts/google-noto-emoji
install -m 0644 -p fonts/NotoEmoji-Regular.ttf %{buildroot}/usr/share/fonts/google-noto-emoji
mkdir -p %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE1} %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/appdata

%files
%defattr(-,root,root)
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md
%license LICENSE
%{_datadir}/fonts/google-noto-emoji/*.ttf
%{_datadir}/appdata/google-noto-emoji*.xml

%changelog
* Fri Mar 20 2020 songnannan <songnannan2@huawei.com> - 20180814-4
- add gdb in buildrequires

* Fri Nov 22 2019 openEuler Buildteam <buildteam@openeuler.org> - 20180814-3
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:close build

* Thu Sep 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 20180814-2
- Package init
