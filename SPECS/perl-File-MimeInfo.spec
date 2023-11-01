# Run optional tests
%if ! (0%{?rhel})
%{bcond_without perl_File_MimeInfo_enables_optional_test}
%else
%{bcond_with perl_File_MimeInfo_enables_optional_test}
%endif
# Use IO::Scalar to support processing a standard input in a mimetype tool
%{bcond_without perl_File_MimeInfo_enables_stdin}
# Use Pod::Usage to support printing a usage text by a mimetype tool
%{bcond_without perl_File_MimeInfo_enables_usage}

Name:           perl-File-MimeInfo
Version:        0.30
Release:        4%{?dist}
Summary:        Determine file type and open application
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/File-MimeInfo
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/File-MimeInfo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::BaseDir) >= 0.03
BuildRequires:  perl(File::DesktopEntry) >= 0.04
BuildRequires:  perl(File::Spec)
# Optional run-time:
%if %{with perl_File_MimeInfo_enables_stdin}
BuildRequires:  perl(IO::Scalar)
%endif
%if %{with perl_File_MimeInfo_enables_usage}
BuildRequires:  perl(Pod::Usage)
%endif
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
# t/11mimeinfo.t executes ./mimetype that returns an unexpected MIME type
# without shared-mime-info database
BuildRequires:  shared-mime-info 
%if %{with perl_File_MimeInfo_enables_optional_test}
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build cycle: perl-Path-Tiny → perl-Unicode-UTF8 →
# perl-Module-Install-ReadmeFromPod → perl-IO-All → perl-File-MimeInfo
BuildRequires:  perl(Path::Tiny)
%endif
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
# Test::Pod::No404s not used
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(File::BaseDir) >= 0.03
Requires:       perl(File::DesktopEntry) >= 0.04
%if %{with perl_File_MimeInfo_enables_stdin}
Recommends:     perl(IO::Scalar)
%endif
%if %{with perl_File_MimeInfo_enables_usage}
Recommends:     perl(Pod::Usage)
%endif
# It's optional, but without it File::MimeInfo produces an annoying warning
# about a missing /usr/share/mime/globs and returns inaccurate results.
Recommends:     shared-mime-info

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::BaseDir|File::DesktopEntry)\\)$

%description
This module can be used to determine the mime type of a file. It tries to
implement the freedesktop specification for a shared MIME database.

%prep
%setup -q -n File-MimeInfo-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset EXTENDED_TESTING
make test

%files
%doc Changes
%{_bindir}/mimeopen
%{_bindir}/mimetype
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.30-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.30-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.30-1
- 0.30 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-9
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-8
- Perl 5.32 rebuild

* Tue Jun 23 2020 Petr Pisar <ppisar@redhat.com> - 0.29-7
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-4
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-1
- 0.29 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-9
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-5
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Petr Pisar <ppisar@redhat.com> - 0.28-2
- Break build cycle: perl-Path-Tiny → perl-Unicode-UTF8 →
  perl-Module-Install-ReademFromPod → perl-IO-All → perl-File-MimeInfo

* Wed Nov 30 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-1
- 0.28 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-2
- Perl 5.22 rebuild

* Wed Feb 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-1
- 0.27 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-1
- 0.26 bump

* Fri Apr 04 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-1
- 0.25 bump

* Mon Mar 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-1
- 0.22 bump

* Mon Nov 04 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-1
- 0.21 bump

* Wed Oct 09 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-1
- 0.20 bump

* Tue Oct 08 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-1
- 0.19 bump, make is used instead of Build
- Fix RT#89328

* Tue Sep 10 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-1
- 0.18 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.17-1
- 0.17 bump

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.16-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.16-2
- Perl 5.16 rebuild

* Fri Jan 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0.16-1
- bump to 0.16
- remove patch, which is included in new release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15-9
- Perl mass rebuild & apply test fix from cpan RT#66841 & clean spec

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.15-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.15-2
- rebuild for new perl

* Thu Feb 14 2008 Patrice Dumas <pertusus@free.fr> 0.15-1
- update to 0.15, remove upstreamed no-ask patch

* Wed Aug  8 2007 Patrice Dumas <pertusus@free.fr> 0.14-1
- update to 0.14

* Thu Nov 16 2006 Patrice Dumas <pertusus@free.fr> 0.13-3
- add a Requires on shared-mime-info (Bug #215972)

* Wed Oct 11 2006 Patrice Dumas <pertusus@free.fr> 0.13-2
- add an option to launch mimeopen non interactively

* Wed Oct 11 2006 Patrice Dumas <pertusus@free.fr> 0.13-1
- Specfile autogenerated by cpanspec 1.69.
