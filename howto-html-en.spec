%define DATE	20080722
%define    language  English
%define    lang      en
%define format1      html-%{lang}
%define format2      HTML/%{lang}

Summary:	%{language} HOWTO documents (html format) from the Linux Documentation Project
Name:		howto-%{format1}
Version:	%DATE
Release:	8
Group:		Books/Howtos

# lftp ibiblio.org:/pub/Linux/docs/HOWTO/other-formats/html> Linux-html-HOWTOs-%DATE.tar.bz2
Source0:	%{name}.tar

Url:		http://www.linuxdoc.org/docs.html#howto
License:	GPLv2
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

BuildRequires:	howto-utils
Requires:	locales-%{lang}, xdg-utils

%description
Linux HOWTOs are detailed documents which describe a specific aspect of 
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

%prep
%setup -qn %{name}

%install
mkdir -p %{buildroot}%{_docdir}/HOWTO/%{format2}
untar_howtos; makehowtoindex %{lang} %{language} > index.html; cp -a * %{buildroot}%{_docdir}/HOWTO/%{format2}

install -m 755 -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Howto %{language}
Comment=HOWTO documents (html format) from the Linux Documentation Project in %{language}
Exec=xdg-open %{_datadir}/doc/HOWTO/HTML/%{lang}/index.html
Icon=documentation_section
Terminal=false
Type=Application
Categories=Documentation;
EOF

%files
%{_docdir}/HOWTO/%{format2}
%{_datadir}/applications/*.desktop

