Name:		texlive-plautopatch
Version:	64072
Release:	2
Summary:	Automated patches for pLaTeX/upLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/plautopatch
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plautopatch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plautopatch.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Japanese pLaTeX/upLaTeX formats and packages often conflict
with other LaTeX packages which are unaware of pLaTeX/upLaTeX.
In the worst case, such packages throw a fatal error or end up
with a wrong output. The goal of this package is that there
should be no need to worry about such incompatibilities,
because specific patches are loaded automatically whenever
necessary. This helps not only to simplify source files, but
also to make the appearance of working pLaTeX/upLaTeX sources
similar to those of ordinary LaTeX ones.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/plautopatch
%doc %{_texmfdistdir}/doc/latex/plautopatch

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
