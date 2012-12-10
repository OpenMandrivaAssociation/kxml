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
Version:        2.2.2
Release:        10
Summary:        Small XML pull parser
License:        BSD
URL:            http://kxml.sourceforge.net/
Group:          Development/Java
Source0:        http://dl.sourceforge.net/sourceforge/kxml/kxml2-src-2.2.2.zip
Source1:        http://repo1.maven.org/maven2/net/sf/kxml/kxml2/2.2.2/kxml2-2.2.2.pom
BuildRequires:  jpackage-utils >= 0:1.7.4
BuildRequires:  java-devel >= 0:1.5.0
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  xpp3 >= 0:1.1.3.1
Requires:  java >= 0:1.5.0
Requires:  xpp3
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires(post):   jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
kXML is a small XML pull parser, specially designed for constrained
environments such as Applets, Personal Java or MIDP devices.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description    javadoc
API documentation for %{name}.

%prep
%setup -q -c
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath xpp3) lib/xmlpull_1_1_3_1.jar

%build
ant

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

%add_to_maven_depmap net.sf.kxml %{name}2 %{version} JPP %{name}
install -m 644 %{SOURCE1} \
        $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}2-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 644 dist/%{name}2-min-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-min.jar

# javadoc
install -p -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr www/kxml2/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%doc license.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%defattr(-,root,root,-)
%doc license.txt
%{_javadocdir}/%{name}



%changelog
* Sun Nov 27 2011 Guilherme Moro <guilherme@mandriva.com> 2.2.2-10
+ Revision: 734059
- rebuild
- imported package kxml

