# revision 20842
# category Package
# catalog-ctan /macros/latex/contrib/sphack
# catalog-date 2010-12-23 15:10:24 +0100
# catalog-license other-nonfree
# catalog-version undef
Name:		texlive-sphack
Version:	20101223
Release:	1
Summary:	Patch LaTeX kernel spacing macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sphack
License:	OTHER-NONFREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sphack.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sphack.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Change the kernel internal \@bsphack/\@esphack so that it is
also invisible in vertical mode.

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
%{_texmfdistdir}/tex/latex/sphack/sphack.sty
%doc %{_texmfdistdir}/doc/latex/sphack/sphack-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sphack/sphack-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
