Name:		texlive-greek-inputenc
Version:	66634
Release:	1
Summary:	Greek encoding support for inputenc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/greek/greek-inputenc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-inputenc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-inputenc.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/greek-inputenc
%doc %{_texmfdistdir}/doc/latex/greek-inputenc

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
