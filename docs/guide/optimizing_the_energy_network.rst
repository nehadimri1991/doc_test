.. _optimizing_the_energy_network:

Optimizing the energy network
=============================

Once the energy system has been defined as an object of the EnergyNetworkIndiv class or the EnergyNetworkGroup class
and the model components (and parameters) have been set from the input excel file, the network object could then be
optimized::

    network.optimize(solver='gurobi',
                     envImpactlimit=envImpactlimit,
                     clusterSize=clusterSize,
                     options=optimizationOptions)

The first parameter solver specifies the name of solver to be used for optimization. 'solver' could take the values
'gurobi', 'cbc', 'cplex' or 'glpk'. 'envImpactlimit' denotes the maximum limit for environmental impact. This parameter
becomes relevant in case of multi-objective optimization and would be described in the later sections. For single-objective
optimization set this parameter to a significantly high value which would never be reached (For example: 10^6). 'clusterSize'
is the parameter related to clustered days (if defined). This is an optional parameter and is required only if clustered
days are used. 'options' specifies the command line parameters to be passed to the selected solver. This parameter is
described further in the following section.

Optimization options
--------------------

To be completed

Single-objective optimization
-----------------------------

To be completed

Multi-objective optimization
----------------------------

To be completed

