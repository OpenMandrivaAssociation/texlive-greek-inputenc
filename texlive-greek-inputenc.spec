Name:		texlive-greek-inputenc
Version:	1.2
Release:	1
Summary:	Greek encoding support for inputenc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/greek/greek-inputenc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-inputenc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-inputenc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The bundle provides Macintosh Greek encoding and ISO 8859-7
definition files for use with inputenc.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
