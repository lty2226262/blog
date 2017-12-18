#include <iostream>
#include "main.h"

int main(int argc, char **argv) {
    double init_x = 99012;
    double x = init_x;
    
    Problem pro;
    
    CostFunction* cost_func = new AutoDiffCostFunction<CostFactory, 1, 1>(new CostFactory);
    pro.AddResidualBlock(cost_func, NULL, &x);
    
    Solver::Options opti;
    opti.minimizer_progress_to_stdout = true;
    Solver::Summary sum;
    Solve(opti, &pro, &sum);
    
    std::cout << sum.BriefReport() << "\n";
    std::cout << "x: " << init_x
              << "->" << x
              << "->" << "\n";
    return 0;
}

