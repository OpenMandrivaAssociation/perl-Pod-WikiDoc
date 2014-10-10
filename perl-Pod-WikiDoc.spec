%define upstream_name    Pod-WikiDoc
%define upstream_version 0.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.20
Release:	2

Summary:	Examples of Pod::WikiDoc usage
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-WikiDoc-0.20.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(File::pushd)
BuildRequires:	perl(Getopt::Lucid)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(IPC::Run3)
BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(Probe::Perl)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Balanced)
BuildArch:	noarch

%description
Pod works well, but writing it can be time-consuming and tedious. For
example, commonly used layouts like lists require numerous lines of text to
make just a couple of simple points. An alternative approach is to write
documentation in a wiki-text shorthand (referred to here as _wikidoc_) and
use Pod::WikiDoc to extract it and convert it into its corresponding Pod as
a separate '.pod' file.

Documentation written in wikidoc may be embedded in Pod format blocks, or,
optionally, in specially marked comment blocks. Wikidoc uses simple
text-based markup like wiki websites to indicate formatting and links. (See
the /WIKIDOC MARKUP manpage, below.)

Pod::WikiDoc processes text files (or text strings) by extracting both
existing Pod and wikidoc, converting the wikidoc to Pod, and then writing
the combined document back to a file or standard output.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man?/*
%{perl_vendorlib}/*
%{_bindir}/wikidoc

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.180.0-2mdv2011.0
+ Revision: 655428
- update file list
- rebuild for updated spec-helper

* Thu Nov 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2011.0
+ Revision: 467463
- import perl-Pod-WikiDoc


* Thu Nov 19 2009 cpan2dist 0.18-1mdv
- initial mdv release, generated with cpan2dist

