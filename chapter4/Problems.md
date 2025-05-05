

#### Section 4.1 -- Least-Squares Estimates of Constant Vectors

    1. Using a least-suqares algorithm, fit quadratic and cubic polunomials to the following time series:
        Z: 1, 27, 33, 45, 12, 16, 83, 67, 54,39,23,6,14,15,19,31,37,44,56,60
        Compute the mean-square error in both cases, and plot the results.
        54,39,23,6,14,15,19,31,37,44,56,60
        Compute the mean-square error in both cases, and plot the results.

    2. Repeat Problem 1, assuming the first data point is 10 times better than the last and that intermediate points are weighted in proportion to their positions in sequences.

    3. One more piece of data is to be added to the sequence in Porblme 1.
        Assuming equal weighting of all points, how would a new reading of 25 affect the quadratic curve fit?
        Use a recursive least-squares estimator to find the answer.

    4. Apply recursive estimation to the entire time series of Problem 1, that is, compute a running estimate beginning with the first point and ending with the last.

    5. The vector **x** is related to the vector **y** by the following equation:
            
            $$`
            \begin{matrix}
                y_1 \\
                y_2
            \end{matrix}
            \begin{matrix}
                0 & 1 \\
                3 & 4
            \end{matrix}
            \begin{matrix}
                x_1 \\
                x_2
            \end{matrix}   
            `$$
        Given the following noisy measurements (**z** = **y** + **n**), what is the least squares estimate of **x**?
            z_1 = 0,1,7,8,5,7,9,10,6,4
            z_2 = 10,7,4,5,5,3,0,2,2,4
    6. The measurement sequence in (5) is taken to represent the nonlinear relationship:
        $$`
            z_1 = x_1^2 + x_2 + 5 + n_1
            z_2 = \frac{ x_2^3}{4} + 4 + n_2
        `$$
        Use a Newton-Raphson algorithm to estimate x_1 and x_2.
        What are the statistics of n_1 and n_2?


#### Section 4.2 -- Propagation of the State Estimate and its Uncertainty


#### Section 4.3 -- Discrete-Time Optimal Filters and Predictors


#### Section 4.4 -- Correlated Disturbance Inputs and Measurement Noise


#### Section 4.5 -- Continuous-Time Optimal Filters and Predictors

#### Section 4.6 -- Optimal Nonlinear Estimation

#### Section 4.7 --  Adaptive Filtering



