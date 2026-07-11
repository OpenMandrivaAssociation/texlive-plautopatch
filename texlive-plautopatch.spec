%global tl_name plautopatch
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9q
Release:	%{tl_revision}.1
Summary:	Automated patches for pLaTeX/upLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/plautopatch
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plautopatch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plautopatch.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Japanese pLaTeX/upLaTeX formats and packages often conflict with other
LaTeX packages which are unaware of pLaTeX/upLaTeX. In the worst case,
such packages throw a fatal error or end up with a wrong output. The
goal of this package is that there should be no need to worry about such
incompatibilities, because specific patches are loaded automatically
whenever necessary. This helps not only to simplify source files, but
also to make the appearance of working pLaTeX/upLaTeX sources similar to
those of ordinary LaTeX ones.

