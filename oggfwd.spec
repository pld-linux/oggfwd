Summary:	Small utility to forward Ogg to server icecast
Summary(pl.UTF-8):	Niewielkie narzędzie do przekazywania plików Ogg do serwera icecast
Name:		oggfwd
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://v2v.cc/~j/oggfwd/%{name}-%{version}.tar.gz
# Source0-md5:	00969e60bec7191e55db1026a698419f
Patch0:		%{name}-Makefile.patch
URL:		http://v2v.cc/~j/ffmpeg2theora/oggfwd
BuildRequires:	libogg-devel
BuildRequires:	libshout-devel >= 2.1
BuildRequires:	libvorbis-devel
BuildRequires:	speex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A basic icecast client that is very simple but also very useful for
video streaming.

%description -l pl.UTF-8
Podstawowy klient icecast, który jest bardzo prosty ale także bardzo
użyteczny do streamingu wideo.

%prep
%setup -q
%patch -P0 -p0

%build
%{__make} \
	CFLAGS="%{rpmcflags} -ffast-math -fsigned-char"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
