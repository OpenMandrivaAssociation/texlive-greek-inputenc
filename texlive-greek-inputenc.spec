# revision 31232
# category Package
# catalog-ctan /language/greek/greek-inputenc
# catalog-date 2013-07-18 14:42:28 +0200
# catalog-license lppl
# catalog-version 1.4.1
Name:		texlive-greek-inputenc
Version:	1.4.1
Release:	8
Summary:	Greek encoding support for inputenc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/greek/greek-inputenc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-inputenc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-inputenc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides Macintosh Greek encoding and ISO 8859-7
definition files for use with inputenc.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/greek-inputenc/iso-8859-7.def
%{_texmfdistdir}/tex/latex/greek-inputenc/lgrenc.dfu
%{_texmfdistdir}/tex/latex/greek-inputenc/macgreek.def
%doc %{_texmfdistdir}/doc/latex/greek-inputenc/README
%doc %{_texmfdistdir}/doc/latex/greek-inputenc/README.html
%doc %{_texmfdistdir}/doc/latex/greek-inputenc/lgrenc.dfu.html
%doc %{_texmfdistdir}/doc/latex/greek-inputenc/test-iso-8859-7.pdf
%doc %{_texmfdistdir}/doc/latex/greek-inputenc/test-iso-8859-7.tex
%doc %{_texmfdistdir}/doc/latex/greek-inputenc/test-utf8.pdf
%doc %{_texmfdistdir}/doc/latex/greek-inputenc/test-utf8.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
