%{?_javapackages_macros:%_javapackages_macros}
# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           kxml
Version:        2.3.0
Release:        7.3
Summary:        Small XML pull parser
Group:		Development/Java
License:        MIT
URL:            https://kxml.sourceforge.net/
# ./create-tarball %%{version}
Source0:        kxml-2.3.0-clean.tar.gz
Source1:        http://repo1.maven.org/maven2/net/sf/kxml/kxml2/%{version}/kxml2-%{version}.pom
Source2:	http://repo1.maven.org/maven2/net/sf/kxml/kxml2-min/%{version}/kxml2-min-%{version}.pom
BuildRequires:  java-devel
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  xpp3 >= 0:1.1.3.1
Requires:       java
Requires:       xpp3 >= 0:1.1.3.1

BuildArch:      noarch

%description
kXML is a small XML pull parser, specially designed for constrained
environments such as Applets, Personal Java or MIDP devices.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
API documentation for %{name}.

%prep
%setup -q
ln -sf $(build-classpath xpp3) lib/xmlpull_1_1_3_1.jar

%build
ant

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

install -m 644 %{SOURCE1} \
        $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
install -m 644 %{SOURCE2} \
 $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}-min.pom

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}2-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 644 dist/%{name}2-min-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-min.jar

%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}-min.pom %{name}-min.jar

# javadoc
install -p -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr www/kxml2/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files -f .mfiles
%doc license.txt
%{_javadir}/*.jar

%files javadoc
%doc license.txt
%{_javadocdir}/%{name}

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Michal Srb <msrb@redhat.com> - 2.3.0-2
- Clean up tarball
- Drop group tag
- Fix R

* Thu Jan 24 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-1
- Update to upstream version 2.3.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 30 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.2-11
- Fix license tag
- Add missing Requires

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2.2-9
- Adapt to current guidelines.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 9 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> 2.2.2-7
- Fix pom dependency from xmlpull to xpp3

* Wed Dec 8 2010 Alexander Kurtakov <akurtako@redhat.com> 2.2.2-6
- Remove versioned jar and javadoc.
- Fix pom name.

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 2.2.2-5
- Fix Summary and description.
- Fix line length.
- Use pom from the URL.

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 2.2.2-4
- Adapt for Fedora.

* Mon Dec 08 2008 Will Tatam <will.tatam@red61.com> 2.2.2-3
- Auto rebuild for JPackage 5 in mock

* Wed May 07 2008 Ralph Apel <r.apel@r-apel.de> 0:2.2.2-2jpp
- Add xpp3 (B)R

* Wed May 07 2008 Ralph Apel <r.apel@r-apel.de> 0:2.2.2-1jpp
- 2.2.2

* Thu Aug 26 2004 Fernando Nasser <fnasser@redhat.com> 0:2.1.8-4jpp
- Pro-forma rebuild with Ant 1.6.2

* Mon Jan 26 2004 David Walluck <david@anti-microsoft.org> 0:2.1.8-3jpp
- remove fractal reference

* Sun Jan 25 2004 David Walluck <david@anti-microsoft.org> 0:2.1.8-2jpp
- fix license

* Sun Jan 25 2004 David Walluck <david@anti-microsoft.org> 0:2.1.8-1jpp
- release
