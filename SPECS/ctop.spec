%define debug_package %{nil}

%global gh_user bcicen

Name:           ctop
Version:        0.7.3
Release:        1%{?dist}
Summary:        Top-like interface for Docker container metrics
Group:          Applications/System
License:        MIT
URL:            https://ctop.sh
BuildRequires:  git golang

%description
ctop provides a concise and condensed overview of real-time metrics for
multiple containers as well as an single container view for inspecting
a specific container.

%prep
wget https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz
mkdir -p %{_builddir}/src/github.com/%{gh_user}/
cd %{_builddir}/src/github.com/%{gh_user}/
mv %{_builddir}/%{name}-%{version} %{name}
mkdir -p %{_builddir}/%{name}-%{version}
cd %{name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
go get -u github.com/golang/dep/cmd/dep
cd %{_builddir}/src/github.com/%{gh_user}/%{name}
GO111MODULE=on go install

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Sun Jan 5 2020 Jamie Curnow <jc@jc21.com> 0.7.3-1
- v0.7.3

* Fri Jan 25 2019 Jamie Curnow <jc@jc21.com> 0.7.2-1
- Updated version

* Wed Sep 12 2018 Jamie Curnow <jc@jc21.com> 0.7.1-1
- Initial Spec

