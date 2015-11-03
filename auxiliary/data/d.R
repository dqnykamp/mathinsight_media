
library(deSolve)

run_logistic = function(r=0.1, K=1000, p0=100, tmax=100, nt=101) {
    # simulate a logistic model

    # arguments:
    # r: low density growth rate
    # K: carrying capacity
    # p0: initial condition for population
    # tmax: maximum time for simulation
    # nt: number of time points to calculate solution

    # all arguments have default values and so are optional.

    # For example, to simulate with default arguments
    # run_logistic()
    
    # For example, to run and specify logistic paramters and initial conditions
    # run_logistic(p0=500, r=0.05, K=10000)
    # To run same simulation but for longer time
    # run_logistic(p0=500, r=0.05, K=10000, tmax=200)


    # function defining the right hand side of the differential equation
    # dp/dt = r*p(1-p/K)
    logistic_f = function(t, y, parms) {
        with(as.list(c(y, parms)), {
            # we assume that parms will include r and K 
            # and that y will contain p
            # so that inside the "with" command, r, K, and p are defined
            dp = r*p*(1-p/K)

            # must output results as a list
            list(dp)
        })
    }

    # define the parameters from the values used in the argument of run_logistic
    parms = c(r=r, K=K)
    
    # initial conditions
    initial = c(p = p0)

    # times where we want to calculate the solution:
    # a total of nt points evenly spaced from t=0 to t=tmax
    times = seq(0, tmax, length = nt)

    # run the simulation
    out = ode(y=initial, times=times, func=logistic_f, parms=parms)

    # plot the results
    plot(out)

    # If you uncomment the following line,
    # the function will return the output values
    # so that you can further analyze them

    #out
}
