Name:		camE
Summary:	A rewrite of the xawtv webcam app, which adds imlib2 support
Summary(pl):	Przepisany z dodaniem wsparcia dla imlib2 program do kamer internetowych xawtv
Version:	1.6
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	0f67f1e077c43d1baa71ff1d6958e959
URL:		http://linuxbrit.co.uk/camE
BuildRequires:	curl-devel
BuildRequires:	freetype1-devel
BuildRequires:	giblib-devel
BuildRequires:	imlib2-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
camE is a rewrite of the xawtv webcam app, which adds imlib2 support
and thus many new possibilities.

%description -l pl
camE jest przepisanym programem do kamer internetowych xawtv, do
kt�rego dodano wsparcie dla imlib2, a co za tym idzie, wiele nowych
mo�liwo�ci.

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
