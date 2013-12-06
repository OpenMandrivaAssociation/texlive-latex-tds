# revision 29325
# category Package
# catalog-ctan /macros/latex/contrib/latex-tds
# catalog-date 2013-03-10 15:09:27 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-latex-tds
Version:	20130310
Release:	5
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
%doc %{_texmfdistdir}/doc/latex/latex-tds/README
%doc %{_texmfdistdir}/doc/latex/latex-tds/README.html
%doc %{_texmfdistdir}/doc/latex/latex-tds/README.pdf
#- source
%doc %{_texmfdistdir}/source/latex/latex-tds/README-docinfo.html
%doc %{_texmfdistdir}/source/latex/latex-tds/README.asciidoc
%doc %{_texmfdistdir}/source/latex/latex-tds/build.pl
%doc %{_texmfdistdir}/source/latex/latex-tds/lib/adjust_checksum.pl
%doc %{_texmfdistdir}/source/latex/latex-tds/lib/ziptimetree.pl
%doc %{_texmfdistdir}/source/latex/latex-tds/license/adjust_checksum/lppl.txt
%doc %{_texmfdistdir}/source/latex/latex-tds/license/latex-tds/lppl.txt
%doc %{_texmfdistdir}/source/latex/latex-tds/license/ziptimetree/lgpl.txt
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/amsclass.dtx.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/amsfndoc.def.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/amsfndoc.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/amsldoc.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/changes.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/encguide.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/hebrew.fdd.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/logmac.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/source2e.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/tlc2.err.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/trapman.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/tripman.tex.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/utf8ienc.dtx.diff
%doc %{_texmfdistdir}/source/latex/latex-tds/patch/webman.tex.diff
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc source %{buildroot}%{_texmfdistdir}
