Name:		texlive-textualicomma
Version:	48474
Release:	2
Summary:	Use the textual comma character as decimal separator in math mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/textualicomma
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textualicomma.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textualicomma.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textualicomma.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is based on the icomma package, and intended as a
solution for situations where the text comma character discerns
from the math comma character, e. g. when fonts whithout math
support are involved. Escaping to text mode every time a comma
is used in math mode may slow down the compilation process.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/textualicomma
%{_texmfdistdir}/tex/latex/textualicomma
%doc %{_texmfdistdir}/doc/latex/textualicomma

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
