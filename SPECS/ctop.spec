%define debug_package %{nil}

%global gh_user bcicen

Name:           ctop
Version:        0.7.7
Release:        1
Summary:        Top-like interface for Docker container metrics
Group:          Applications/System
License:        MIT
URL:            https://ctop.sh
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
ctop provides a concise and condensed overview of real-time metrics for
multiple containers as well as an single container view for inspecting
a specific container.

%prep
%setup -q -n %{name}-%{version}

%build
export GO111MODULE=on
go build -o bin/ctop

%install
install -Dm0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Wed Mar 23 2022 Jamie Curnow <jc@jc21.com> 0.7.7-1
- v0.7.7

* Mon Jun 14 2021 Jamie Curnow <jc@jc21.com> 0.7.6-1
- v0.7.6

* Mon Nov 9 2020 Jamie Curnow <jc@jc21.com> 0.7.5-1
- v0.7.5

* Tue Oct 27 2020 Jamie Curnow <jc@jc21.com> 0.7.4-1
- v0.7.4

* Sun Jan 5 2020 Jamie Curnow <jc@jc21.com> 0.7.3-1
- v0.7.3

* Fri Jan 25 2019 Jamie Curnow <jc@jc21.com> 0.7.2-1
- Updated version

* Wed Sep 12 2018 Jamie Curnow <jc@jc21.com> 0.7.1-1
- Initial Spec
