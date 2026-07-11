%global tl_name greek-inputenc
%global tl_revision 66634

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9
Release:	%{tl_revision}.1
Summary:	Greek encoding support for inputenc
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/greek/greek-inputenc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-inputenc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-inputenc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Input encoding definition files for UTF-8, Macintosh Greek, and ISO
8859-7 enabling the use of literal characters for Greek letters and
symbols with 8-bit TeX engines (pdfLaTeX).

