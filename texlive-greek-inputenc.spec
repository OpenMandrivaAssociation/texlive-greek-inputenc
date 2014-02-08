# revision 15878
# category Package
# catalog-ctan /language/greek/greek-inputenc
# catalog-date 2008-08-21 09:38:31 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-greek-inputenc
Version:	1.2
Release:	3
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
%{_texmfdistdir}/tex/latex/greek-inputenc/macgreek.def
%doc %{_texmfdistdir}/doc/latex/greek-inputenc/test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 752431
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718581
- texlive-greek-inputenc
- texlive-greek-inputenc
- texlive-greek-inputenc
- texlive-greek-inputenc

