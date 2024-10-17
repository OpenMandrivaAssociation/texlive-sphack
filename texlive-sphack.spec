Name:		texlive-sphack
Version:	20842
Release:	2
Summary:	Patch LaTeX kernel spacing macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sphack
License:	OTHER-NONFREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sphack.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sphack.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
