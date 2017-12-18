#include "ceres/ceres.h"

using ceres::AutoDiffCostFunction;
using ceres::CostFunction;
using ceres::Problem;
using ceres::Solver;
using ceres::Solve;

struct CostFactory{
  template <typename T> bool operator()(const T* const x, T* residual) const{
    residual[0] = 10.0 - x[0];
    return true;
  }
};

