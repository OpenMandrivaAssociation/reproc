Name:           reproc
Version:        14.2.0
Release:        1
Summary:        Cross-platform library that simplifies working with external CLI applications from C and C++
Group:          Development/C
License:        MIT
URL:            https://github.com/DaanDeMeyer/reproc
Source0:        https://github.com/DaanDeMeyer/reproc/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
reproc (Redirected Process) is a cross-platform C/C++ library that simplifies starting, stopping and communicating with external programs. 
The main use case is executing command line applications directly from C or C++ code and retrieving their output.
reproc consists out of two libraries: reproc and reproc++. reproc is a C99 library that contains the actual code for working with external programs. 
reproc++ depends on reproc and adapts its API to an idiomatic C++11 API.  It also adds a few extras that simplify working with external programs from C++.

%prep
%autosetup -p1

%build

%cmake  \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
        -DBUILD_SHARED_LIBS=ON \
        -DREPROCXX=ON \
        -DREPROC_TEST=ON
       
%make_build

%install

%make_install -C build

%files
