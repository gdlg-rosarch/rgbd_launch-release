# Script generated with Bloom
pkgdesc="ROS - Launch files to open an RGBD device and load all nodelets to convert raw depth/RGB/IR streams to depth images, disparity images, and (registered) point clouds."
url='http://www.ros.org/wiki/rgbd_launch'

pkgname='ros-kinetic-rgbd-launch'
pkgver='2.2.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-depth-image-proc'
'ros-kinetic-image-proc'
'ros-kinetic-nodelet'
'ros-kinetic-rostest'
'ros-kinetic-tf2-ros'
)

depends=('ros-kinetic-depth-image-proc'
'ros-kinetic-image-proc'
'ros-kinetic-nodelet'
'ros-kinetic-tf2-ros'
)

conflicts=()
replaces=()

_dir=rgbd_launch
source=()
md5sums=()

prepare() {
    cp -R $startdir/rgbd_launch $srcdir/rgbd_launch
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

