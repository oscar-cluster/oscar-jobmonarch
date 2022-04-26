Summary: Slurm Interface for Python
Name: python3.6-pyslurm
#Name: python-slurm
Version: 20.11.8.0
URL: http://www.gingergeeks.co.uk/pyslurm/index.html
Release: 1%{?dist}
License: GPL
Packager: Olivier LAHAYE <olivier.lahaye@cea.fr>
Group: Development/Languages
Source: v20.11.8-1.tar.gz
#Patch0: pyslurm_sphinx_theme.patch
#Patch1: pyslurm_doc_no_python_github.patch
#Patch2: pyslurm_doc_version.patch
BuildRoot: %{_tmppath}/%{name}
Provides: python3-pyslurm
BuildRequires: python3-devel => 3 python3-Cython >= 0.28 python3-sphinx >= 1.1 slurm-devel >= 20.11.7

%description
PySLURM is a Python/Cython extension module to the Simple Linux Unified
Resource Manager (SLURM) API. It can be used to contact slurmctld.
SLURM is typically used on HPC clusters such as those listed on the TOP500
but can used on the smallest to the largest cluster. 

%prep
%setup -q -n pyslurm-20.11.8-1
#patch0 -p1

%build
%{__python3} setup.py build --slurm=%{_prefix}
#sed -i -e '/sphinx.ext.githubpages/d' doc/source/conf.py
(cd doc; PYTHONPATH=../build/lib.linux-x86_64-%{python3_version}/:%{python3_sitelib} \
 make html SPHINXBUILD=sphinx-build-3;\
 PYTHONPATH=../build/lib.linux-x86_64-%{python3_version}/:%{python3_sitelib} \
 make man SPHINXBUILD=sphinx-build-3)

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install --prefix=%{_prefix} --optimize=2 --root=%buildroot --install-lib=%{python3_sitearch}
install -d %{buildroot}%{_mandir}/man1
install -m 644 doc/build/man/pyslurm.1 %{buildroot}%{_mandir}/man1/

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc CONTRIBUTORS.rst COPYING.txt README.rst THANKS.rst
%doc doc/build/html
%doc examples
%{python3_sitearch}/pyslurm*
%{_mandir}/man1/pyslurm.1*

%changelog
* Fri Jan  7 2022 Olivier Lahaye <olivier.lahaye@cea.fr> 20.11.8.0-1
- New version
* Fri Apr 20 2018 Olivier Lahaye <olivier.lahaye@cea.fr> 17.11.0.7-1
- New version
* Thu Jun 22 2017 Olivier Lahaye <olivier.lahaye@cea.fr> 17.02-1
- New version
* Fri Mar 04 2016 Olivier Lahaye <olivier.lahaye@cea.fr> 15.08.2-1
- New version
* Tue Jan 14 2014 Olivier Lahaye <olivier.lahaye@cea.fr> 2.5.6-1
- Initial packaging
