%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name binary-extensions

Summary:       List of binary file extensions
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.3.1
Release:       2%{?dist}
License:       MIT
URL:           https://github.com/sindresorhus/binary-extensions
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
List of binary file extensions

The list is just a JSON file and can be used wherever.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr binary-extensions.json package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%license license
%{nodejs_sitelib}/%{npm_name}

%changelog
* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 1.3.1-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 1.3.1-1
- Initial package
