Name:		texlive-sphack
Version:	20190228
Release:	1
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
%{_texmfdistdir}/tex/latex/sphack
%doc %{_texmfdistdir}/doc/latex/sphack

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
