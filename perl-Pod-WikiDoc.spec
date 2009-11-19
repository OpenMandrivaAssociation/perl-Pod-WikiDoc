%define upstream_name    Pod-WikiDoc
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Examples of Pod::WikiDoc usage
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Cwd)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::pushd)
BuildRequires: perl(Getopt::Lucid)
BuildRequires: perl(IO::String)
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(Parse::RecDescent)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Probe::Perl)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Balanced)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/wikidoc
/usr/share/man/man1/wikidoc.1.lzma

