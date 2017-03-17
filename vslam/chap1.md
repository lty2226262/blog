#vSlam

##1 Intro

slam - simultaneous localization and mapping

* a mobile base equipped with sensors
* no priori knowledge
* build maps when they're moving
* estimate their own movement

recommend books:

1. ***probabilistic robotics***
2. ***multiple view geometry in computer vision***
3. ***state estimation for robotics: a matrix-lie-group approach***

a slam system divided into 4 modules:

1. visual odometry
2. back-end optimization
3. map building
4. loopback detecion

key to practice:

1. A is invertible, which means that the rank of a m-by-m matrix equals m.
2. multivariate normal distribution: is a generalization of the one-dimensional normal distribution to higher dimensions. The multivariate normal distribution of a k-dimensional random vector <img src="http://latex.codecogs.com/gif.latex?x%3D%5Bx_1%2C%20x_2%2C%20...%2C%20x_k%5D" \> can be written in the following notation:

 <img src="http://latex.codecogs.com/gif.latex?x\sim%20N_k(\mu,%20\Sigma)" \>
3.  class: classes are an expanded concept of data structures, like data structures, they can contain data members, but they can also contain functions as members.

  template: a template is a blueprint or formula for creating a generic class or a function.

  Function Template: The general form of a template function definition is shown here:

        template <class type> ret-type func-name(parameter list) {
            // body of function
          }
      function template SAMPLE:
        #include <iostream>
        #include <string>

        using namespace std;

        template <typename T>
        inline T const& Max (T const& a, T const& b)  {
         return a < b ? b:a;
        }

        int main () {

         int i = 39;
         int j = 20;
         cout << "Max(i, j): " << Max(i, j) << endl;

         double f1 = 13.5;
         double f2 = 20.7;
         cout << "Max(f1, f2): " << Max(f1, f2) << endl;

         string s1 = "Hello";
         string s2 = "World";
         cout << "Max(s1, s2): " << Max(s1, s2) << endl;

         return 0;
        }
      class template SAMPLE:
        template <class type> class class-name {
         .
         .
         .
        }
      A class template SAMPLE:
        #include <iostream>
        #include <vector>
        #include <cstdlib>
        #include <string>
        #include <stdexcept>

        using namespace std;

        template <class T>
        class Stack {
           private:
              vector<T> elems;     // elements

           public:
              void push(T const&);  // push element
              void pop();               // pop element
              T top() const;            // return top element
              bool empty() const{       // return true if empty.
                 return elems.empty();
              }
        };

        template <class T>
        void Stack<T>::push (T const& elem) {
           // append copy of passed element
           elems.push_back(elem);    
        }

        template <class T>
        void Stack<T>::pop () {
           if (elems.empty()) {
              throw out_of_range("Stack<>::pop(): empty stack");
           }

           // remove last element
           elems.pop_back();         
        }

        template <class T>
        T Stack<T>::top () const {
           if (elems.empty()) {
              throw out_of_range("Stack<>::top(): empty stack");
           }

           // return copy of last element
           return elems.back();      
        }

        int main() {
           try {
              Stack<int>         intStack;  // stack of ints
              Stack<string> stringStack;    // stack of strings

              // manipulate int stack
              intStack.push(7);
              cout << intStack.top() <<endl;

              // manipulate string stack
              stringStack.push("hello");
              cout << stringStack.top() << std::endl;
              stringStack.pop();
              stringStack.pop();
           }catch (exception const& ex) {
              cerr << "Exception: " << ex.what() <<endl;
              return -1;
           }
        }

      The C++ STL (Standard Template Library) is a powerful set of C++ template classes to provides general-purpose templatized classes and functions that implement many popular and commonly used algorithms and data structures like vectors, lists, queues, and stacks.

      At the core of the C++ Standard Template Library are following three well-structured components:

      <table class="table table-bordered">
      <tbody><tr>
      <th width="30%">Component</th>
      <th>Description</th>
      </tr>
      <tr>
      <td>Containers</td>
      <td>Containers are used to manage collections of objects of a certain kind. There are several different types of containers like  deque, list, vector, map etc.</td>
      </tr>
      <tr>
      <td>Algorithms</td>
      <td>Algorithms act on containers. They provide the means by which you will perform initialization, sorting, searching, and transforming of the contents of containers.</td>
      </tr>
      <tr>
      <td>Iterators</td>
      <td>Iterators are used to step through the elements of collections of objects. These collections may be containers or subsets of containers.</td>
      </tr>
      </tbody></table>
4. C++11 new changes:

  lambda expressions

  automatic type deduction and decltype

  uniform initialization syntax

  deleted and defaulted functions

  nullptr

  delegating constructors

  rvalue references

  http://blog.smartbear.com/c-plus-plus/the-biggest-changes-in-c11-and-why-you-should-care/
