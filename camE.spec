Summary:	A rewrite of the xawtv webcam app, which adds imlib2 support
Summary(pl.UTF-8):   Przepisany z dodaniem wsparcia dla imlib2 program do kamer internetowych xawtv
Name:		camE
Version:	1.9
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	8bdc049b01cd32088eef8cccf3c096ab
URL:		http://linuxbrit.co.uk/camE/
BuildRequires:	curl-devel
BuildRequires:	freetype1-devel
BuildRequires:	giblib-devel
BuildRequires:	imlib2-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
camE is a rewrite of the xawtv webcam app, which adds imlib2 support
and thus many new possibilities.

%description -l pl.UTF-8
camE jest przepisanym programem do kamer internetowych xawtv, do
którego dodano wsparcie dla imlib2, a co za tym idzie, wiele nowych
możliwości.

%prep
%setup -q

%build
perl -pi -e 's/-O3 -g -Wall/%{rpmcflags}/' Makefile
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS *.style example.camErc*
%attr(755,root,root) %{_bindir}/%{name}
