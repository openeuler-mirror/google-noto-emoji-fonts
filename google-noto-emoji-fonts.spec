%global fontname google-noto-emoji
 
Name:           %{fontname}-fonts
Version:        20200916
Release:        2
Summary:        Color and Black-and-White noto emoji fonts
 
License:        OFL and ASL 2.0
URL:            https://github.com/googlei18n/noto-emoji
Source0:        https://github.com/googlei18n/noto-emoji/archive/v2020-09-16-unicode13_1.tar.gz
Source1:        %{fontname}.metainfo.xml
Source2:        %{fontname}-color.metainfo.xml
 
Patch0:         noto-emoji-build-all-flags.patch
Patch1:         noto-emoji-use-gm.patch
Patch2:         noto-emoji-use-system-pngquant.patch 
 
BuildArch:          noarch

BuildRequires:      gcc
BuildRequires:      fontpackages-devel fonttools python3-fonttools nototools python3-devel
BuildRequires:      GraphicsMagick pngquant zopfli cairo-devel python3-nototools gdb
 
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
%autosetup -n noto-emoji-2020-09-16-unicode13_1 -p1
 
rm -rf third_party/pngquant
 
%build
export LANG=C.UTF-8
 
%make_build OPT_CFLAGS="$RPM_OPT_FLAGS" BYPASS_SEQUENCE_CHECK='True'
 
%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p NotoColorEmoji.ttf %{buildroot}%{_fontdir}
install -m 0644 -p fonts/NotoEmoji-Regular.ttf %{buildroot}%{_fontdir}
 
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
* Wed May 26 2021 liuyumeng <liuyumeng5@huawei.com> - 20200916-2
- Add a BuildRequires for gcc

* Thu Oct 29 2020 jinzhimin <jinzhimin2@huawei.com> - 20200916-1
- update to 20200916

* Fri Mar 20 2020 songnannan <songnannan2@huawei.com> - 20180814-4
- add gdb in buildrequires

* Fri Nov 22 2019 openEuler Buildteam <buildteam@openeuler.org> - 20180814-3
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:close build

* Thu Sep 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 20180814-2
- Package init
