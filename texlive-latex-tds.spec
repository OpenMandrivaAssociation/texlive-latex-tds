Name:		texlive-latex-tds
Version:	20170414
Release:	1
Summary:	A structured copy of the LaTeX distribution
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex-tds
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-tds.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-tds.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-tds.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This bundle provides a set of zip file modules containing TDS-
compliant trees for items of the LaTeX distribution (both the
base system and required packages), together with 'user-
friendly' documentation (PDF files with navigation support
using bookmarks and links). A further module (knuth) performs
the same service for Knuth's software distribution.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex-tds
#- source
%doc %{_texmfdistdir}/source/latex/latex-tds

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc source %{buildroot}%{_texmfdistdir}
