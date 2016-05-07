Name:           ros-indigo-rgbd-launch
Version:        2.1.2
Release:        0%{?dist}
Summary:        ROS rgbd_launch package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/rgbd_launch
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-depth-image-proc
Requires:       ros-indigo-image-proc
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-depth-image-proc
BuildRequires:  ros-indigo-image-proc
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-tf

%description
Launch files to open an RGBD device and load all nodelets to convert raw
depth/RGB/IR streams to depth images, disparity images, and (registered) point
clouds.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat May 07 2016 Piyush Khandelwal <piyushk@gmail.com> - 2.1.2-0
- Autogenerated by Bloom

* Mon Nov 16 2015 Piyush Khandelwal <piyushk@gmail.com> - 2.1.1-0
- Autogenerated by Bloom

