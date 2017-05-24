#ifndef FRAME_H
#define FRAME_H

#include "myslam/common_include.h"
#include "myslam/camera.h"

namespace myslam{
  class Frame{
  public:
    typedef std::shared_ptr<Frame> Ptr;
    unsigned long id_; //id of this frame
    double time_stamp_; //when it is recorded
    SE3 T_c_w; //transform from world to camera
    Camera::Ptr camera_; //Pinhole RGB-D camera model
    Mat color_, depth_;

  public:
    Frame();
    Frame( long id, double time_stamp = 0, SE3 T_c_w = SE3(), Camera::Ptr camera = nullptr, Mat color = Mat(), Mat depth = Mat() );
    ~Frame();

    //factory function
    static Frame::Ptr creatFrame();

    //find the depth in depth map
    double findDepth( const cv::KeyPoint& kp );

    // Get Camera Center
    Vector3d getCamCenter() const;

    // check if a point is in this frame
    bool isInFrame( const Vector3d& pt_world);
  }
}

#endif
