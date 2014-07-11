# revision 20842
# category Package
# catalog-ctan /macros/latex/contrib/sphack
# catalog-date 2010-12-23 15:10:24 +0100
# catalog-license other-nonfree
# catalog-version undef
Name:		texlive-sphack
Version:	20101223
Release:	8
Summary:	Patch LaTeX kernel spacing macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sphack
License:	OTHER-NONFREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sphack.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sphack.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Change the kernel internal \@bsphack/\@esphack so that it is
also invisible in vertical mode.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sphack/sphack.sty
%doc %{_texmfdistdir}/doc/latex/sphack/sphack-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sphack/sphack-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101223-2
+ Revision: 756153
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101223-1
+ Revision: 719563
- texlive-sphack
- texlive-sphack
- texlive-sphack
- texlive-sphack

