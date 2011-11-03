# revision 24252
# category Package
# catalog-ctan /macros/latex/contrib/latex-tds
# catalog-date 2011-10-09 16:42:04 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-latex-tds
Version:	20111009
Release:	1
Summary:	A structured copy of the LaTeX distribution
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex-tds
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-tds.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-tds.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This bundle provides a set of zip file modules containing TDS-
compliant trees for items of the LaTeX distribution (both the
base system and required packages), together with 'user-
friendly' documentation (PDF files with navigation support
using bookmarks and links). A further module (knuth) performs
the same service for Knuth's software distribution.

#-----------------------------------------------------------------------
%files
#- source
%doc %{_texmfdistdir}/source/latex/latex-tds/build.pl
%doc %{_texmfdistdir}/source/latex/latex-tds/lib/adjust_checksum.pl
%doc %{_texmfdistdir}/source/latex/latex-tds/lib/ziptimetree.pl
%doc %{_texmfdistdir}/source/latex/latex-tds/license/lppl.txt
%doc %{_texmfdistdir}/source/latex/latex-tds/license/ziptimetree/lgpl.txt
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/amsclass.dtx.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/amsldoc.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/changes.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/encguide.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/lb2.err.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/logmac.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/source2e.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/tlc2.err.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/trapman.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/tripman.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/utf8ienc.dtx.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/webman.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/readme.txt
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/ams.drv
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/babel.tex
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/doc_lppl.tex
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/docstrip.cfg
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/errata.all
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/errata.cfg
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/errata.drv
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/errorlog.drv
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/etex_man.drv
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/greek-usage.tex
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/hyperref.cfg
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/knuth.drv
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/ltnews.cfg
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/ltnews.tex
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/ltugboat.cfg
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/ltxcheck.drv
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/ltxdoc.cfg
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/ltxguide.cfg
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/lualatex-tds.ini
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/lualatex-tds2.ini
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/manual.cfg
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/pdflatex-tds.ini
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/psnfss2e.drv
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/tdsguide.cfg
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/tools-overview.cls
%doc %{_texmfdistdir}/source/latex/latex-tds/tex/tools.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
