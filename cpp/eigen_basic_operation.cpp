#include <iostream>
#include <ctime>
using namespace std;

//Eigen part
#include <Eigen/Core>
//dense matrix algebraic operation(inverse, det .et al)
#include <Eigen/Dense>

#define MATRIX_SIZE 50

int main(int argc, char **argv) {
    //Eigen is based on matrixes. it is a template class. its former 3 parameters are: type, rows, columns
    //declare a 2x3 float matrix
    Eigen::Matrix<float, 2, 3> matrix23;
     //Eigen define a good many types by function typedef, and they are implemented by matrix
    //for example, vector3d is Eigen::Matrix<double,3,1> in fact
    Eigen::Vector3d v_3d;
    //matrix3d is Eigen::Matrix<double,3,3> in fact
    Eigen::Matrix3d matrix_33 = Eigen::Matrix3d::Zero(); //initialize to Zero
    //if the size is not sure, we could use the dynamic sizes matrix
    Eigen::Matrix< double, Eigen::Dynamic, Eigen::Dynamic > matrix_dynamic;
    //to be easier
    Eigen::MatrixXd matrix_x;
    //no more examples in detail

    //manupate the matrix
    //input data
    matrix23 << 1,2,3,4,5,6;
    //output
    cout << matrix23 << endl;

    //access the elements by ()
    for (int i=0; i<1; i++)
      for (int j=0; j<2; j++)
	cout<<matrix23(i,j)<<endl;

    v_3d << 3,2,1;
    //multiply a matrix with a vector
    //we cannot fuse various types, belows are wrong
//     Eigen::Matrix<double,2,1> result_wrong_type = matrix23 * v_3d;

    //we must explicitly cast
    Eigen::Matrix<double,2,1>result = matrix23.cast<double>() * v_3d;
    cout << result <<endl;

    //we cannot mistake the dimension
    //Eigen::Matrix<double,2,3>result_wrong_dimension=matrix_23.cast<double>() * v_3d;

    //some matrix operations
    //+ - * /
    matrix_33 = Eigen::Matrix3d::Random();
    cout << matrix_33 << endl <<endl;

    cout << matrix_33.transpose() << endl; // transpose
    cout << matrix_33.sum() << endl; //every element sum
    cout << matrix_33.trace() << endl; //trace of matrix
    cout << matrix_33 * 10 << endl; // number multiply
    cout << matrix_33.inverse() << endl; //inverse
    cout << matrix_33.determinant() << endl; //determinant

    //eigen value
    Eigen::SelfAdjointEigenSolver<Eigen::Matrix3d> eigen_solver (matrix_33);
    cout << "Eigen values = " << eigen_solver.eigenvalues() <<endl;
    cout << "Eigen vectors = " << eigen_solver.eigenvectors() << endl;

    //solve the equation
    //we solve the answer of Matrix * x = v_Nd
    //the size of N is define at the top, values are defined randomly
    //less computation than inverse

    Eigen::Matrix<double, MATRIX_SIZE, MATRIX_SIZE> matrix_NN;
    matrix_NN = Eigen::MatrixXd::Random( MATRIX_SIZE, MATRIX_SIZE );
    Eigen::Matrix<double, MATRIX_SIZE, 1> v_Nd;
    v_Nd = Eigen::MatrixXd::Random(MATRIX_SIZE,1);

    clock_t time_stt = clock();//compute the time
    //compute the inverse directly
    Eigen::Matrix<double, MATRIX_SIZE, 1> x = matrix_NN.inverse()*v_Nd;
    cout << "time use is normal inverse is " << 1000 * (clock() - time_stt)/(double)CLOCKS_PER_SEC << "ms" << endl;
//     cout << x <<endl;

    //compute by QR compsition, much faster
    time_stt = clock();
    x = matrix_NN.colPivHouseholderQr().solve(v_Nd);
    cout << "time use in Qr compsition is " << 1000 * (clock() - time_stt) / (double) CLOCKS_PER_SEC << "ms" << endl;
//     cout << x << endl;

    return 0;
}
