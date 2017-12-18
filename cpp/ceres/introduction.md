# Ceres notes

## introduction

$$
\begin{split}\min_{\mathbf{x}} &\quad \frac{1}{2}\sum_{i} \rho_i\left(\left\|f_i\left(x_{i_1}, ... ,x_{i_k}\right)\right\|^2\right) \\
\text{s.t.} &\quad l_j \le x_j \le u_j\end{split}
$$

`ResidualBlock` - 
$$
\rho_i\left(\left\|f_i\left(x_{i_1}, ... ,x_{i_k}\right)\right\|^2\right)
$$
$\rho_i$ is a`CostFunction` that depends on the parameter blocks $\left[x_{i_1},... , x_{i_k}\right]$. We refer to such a group of small scalars as a `ParameterBlock`.For example the quaternion and translation vector. Of course a `ParameterBlock` can just be a single parameter. $l_j$ and $u_j$ are bounds on the parameter block $x_j$.

$\rho_i$ is a `LossFunction`. Reduce the influence of outliers.

## Hello World!

FInding the min of the function
$$
\frac{1}{2}(10-x)^2
$$
So, $f(x) = 10 -x$, $\rho(x) = x$.



CMakeLists is:

```cmake
cmake_minimum_required(VERSION 2.6)
project(ceres_study)

find_package(Ceres REQUIRED)
include_directories(${CERES_INCLUDE_DIRS})

add_executable(ceres_study main.cpp)
target_link_libraries(ceres_study ${CERES_LIBRARIES})
```





```cpp
#include "ceres/ceres.h"

using ceres::AutoDiffCostFunction;
using ceres::CostFunction;
using ceres::Problem;
using ceres::Solver;
using ceres::Solve;

struct CostFunctor {
   template <typename T>
   bool operator()(const T* const x, T* residual) const {
     residual[0] = T(10.0) - x[0];
     return true;
   }
};
```



The important thing to note here is that `operator()` is a templated method, which assumes that all its inputs and outputs are of some type `T`. The use of templating here allows Ceres to call`CostFunctor::operator<T>()`, with `T=double` when just the value of the residual is needed, and with a special type `T=Jet` when the Jacobians are needed. In [Derivatives](http://ceres-solver.org/nnls_tutorial.html#section-derivatives) we will discuss the various ways of supplying derivatives to Ceres in more detail.

```Cpp
int main(int argc, char** argv) {
  google::InitGoogleLogging(argv[0]);

  // The variable to solve for with its initial value.
  double initial_x = 5.0;
  double x = initial_x;

  // Build the problem.
  Problem problem;

  // Set up the only cost function (also known as residual). This uses
  // auto-differentiation to obtain the derivative (jacobian).
  CostFunction* cost_function =
      new AutoDiffCostFunction<CostFunctor, 1, 1>(new CostFunctor);
  problem.AddResidualBlock(cost_function, NULL, &x);

  // Run the solver!
  Solver::Options options;
  options.linear_solver_type = ceres::DENSE_QR;
  options.minimizer_progress_to_stdout = true;
  Solver::Summary summary;
  Solve(options, &problem, &summary);

  std::cout << summary.BriefReport() << "\n";
  std::cout << "x : " << initial_x
            << " -> " << x << "\n";
  return 0;
}
```

