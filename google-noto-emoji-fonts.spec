Name:               google-noto-emoji-fonts
Version:            20180814
Release:            2
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
BuildRequires:      GraphicsMagick pngquant zopfli cairo-devel python2-nototools

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
export LANG=C.UTF-8
%make_build OPT_CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p %{buildroot}%{_fontdir}
chmod 755 %{buildroot}%{_fontdir}

cp NotoColorEmoji.ttf %{buildroot}%{_fontdir}
chmod 644 %{buildroot}%{_fontdir}/NotoColorEmoji.ttf
touch %{buildroot}%{_fontdir}/NotoColorEmoji.ttf

cp fonts/NotoEmoji-Regular.ttf %{buildroot}%{_fontdir}
chmod 644 %{buildroot}%{_fontdir}/NotoEmoji-Regular.ttf
touch %{buildroot}%{_fontdir}/NotoEmoji-Regular.ttf

mkdir -p %{buildroot}%{_datadir}/appdata
cp %{SOURCE1} %{buildroot}%{_datadir}/appdata
chmod 644 %{buildroot}%{_datadir}/appdata/google-noto-emoji.metainfo.xml
touch %{buildroot}%{_datadir}/appdata/google-noto-emoji.metainfo.xml

cp %{SOURCE2} %{buildroot}%{_datadir}/appdata
chmod 644 %{buildroot}%{_datadir}/appdata/google-noto-emoji-color.metainfo.xml
touch %{buildroot}%{_datadir}/appdata/google-noto-emoji-color.metainfo.xml

%changelog
* Thu Sep 19 2019 dongjian <dongjian13@huawei.com> - 20180814-2
- Package init
