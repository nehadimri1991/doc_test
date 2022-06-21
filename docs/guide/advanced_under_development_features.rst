.. _advanced_under_development_features:

Advanced under-development features
===================================

Building model
--------------

A linear RC building model is presently under-development to replace the static space heating demand profiles. A building
model is a grey-box model which is often used to depict the thermal behaviour of a building in a simplified manner. It is
implemented as a custom sink component along with a set of new constraints.

.. image:: ./resources/building_model_oemof.png
      :width: 400
      :alt: building_model_oemof

The specific building model implemented in optihood was proposed and validated in [1] and is characterized by three thermal
spaces:

- wall and building mass
- indoor air
- distribution system

Each thermal space is at a certain temperature at a particular timestep. Moreover, each thermal space has two key parameters
which represent the thermal resistance and thermal capacity. The temperature of each thermal space is influenced by the
temperature of adjascent thermal spaces, heat flow, internal heat gains and ambient weather conditions.

.. image:: ./resources/building_model.png
      :width: 600
      :alt: building_model

The parameters and variables of the RC model are described below:

+----------------------------------------------------------------------------------------------------------------------+
| **Parameters**                                                                                                       |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`R_{ind}`           |  Thermal resistance between indoor and wall states [K/kW]                                |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`R_{wall}`          |  Thermal resistance between wall state and outside [K/kW]                                |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`R_{dis}`           |  Thermal resistance between indoor and distribution system states [K/kW]                 |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`C_{ind}`           |  Thermal capacity of the indoor air state [kWh/K]                                        |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`C_{wall}`          |  Thermal capacity of the wall state [kWh/K]                                              |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`C_{dis}`           |  Thermal capacity of the distribution system state [kWh/K]                               |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`gA`                |  Aperture area of the windows [:math:`m^2`]                                              |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`Q^{dis}_{min}`     |  Minimum operating power from the tank to the distribution system [kW]                   |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`Q^{dis}_{max}`     |  Maximum operating power from the tank to the distribution system [kW]                   |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`T^{ind}_{min}`     |  Indoor minimum comfort temperature [°C]                                                 |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`T^{ind}_{max}`     |  Indoor maximum comfort temperature [°C]                                                 |
+---------------------------+------------------------------------------------------------------------------------------+
| **Exogenous input parameters**                                                                                       |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`T^{amb}_{t}`       |  Ambient outside air temperature at :math:`t^{th}` timestep [°C]                         |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`I^{H}_{t}`         |  Total horizontal irradiation at :math:`t^{th}` timestep [kW/:math:`m^2`]                |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`Q^{occ}_{t}`       |  Internal heat gains from occupants at :math:`t^{th}` timestep [kW]                      |
+---------------------------+------------------------------------------------------------------------------------------+
| **Boundary parameters**                                                                                              |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`T^{ind}_{init}`    |  Indoor initial temperature [°C]                                                         |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`T^{wall}_{init}`   |  Wall initial temperature [°C]                                                           |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`T^{dis}_{init}`    |  Distribution system initial temperature [°C]                                            |
+---------------------------+------------------------------------------------------------------------------------------+
| **State variables**                                                                                                  |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`T^{ind}_t`         |  Indoor temperature at :math:`t^{th}` timestep [°C]                                      |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`T^{wall}_t`        |  Wall temperature at :math:`t^{th}` timestep [°C]                                        |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`T^{dis}_t`         |  Distribution system temperature at :math:`t^{th}` timestep [°C]                         |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`\epsilon^{ind}_t`  | Violation of indoor comfort temperature range at :math:`t^{th}` timestep [°C]            |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`\delta^{ind}_t`    |  Violation of indoor final temperature requirement [°C]                                  |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`P^{dis}_t`         |  Electric consumption of the distribution system                                         |
+---------------------------+------------------------------------------------------------------------------------------+
| **Decision variable**                                                                                                |
+---------------------------+------------------------------------------------------------------------------------------+
| :math:`Q^{dis}_t`         | Heating power from the tank to the distribution system at :math:`t^{th}` timestep [kW]   |
+---------------------------+------------------------------------------------------------------------------------------+

The state space equations of the building model are:

.. image:: ./resources/state_space_eq.png
      :width: 600
      :alt: state_space_eq
      :align: center

| The final constraints of the building model are:

.. image:: ./resources/Constraint1.png
      :width: 520
      :alt: constraint1
      :align: center

.. image:: ./resources/Constraint2.png
      :width: 140
      :alt: constraint2
      :align: center

.. image:: ./resources/Constraint3.png
      :width: 300
      :alt: constraint3
      :align: center

.. image:: ./resources/Constraint4.png
      :width: 200
      :alt: constraint4
      :align: center

.. image:: ./resources/Constraint5.png
      :width: 400
      :alt: constraint5
      :align: center

| [1] T. Péan, R. Costa Castelló y J. Salom, Price and carbon-based energy flexibility of residential heating and cooling loads using model predictive control, Sustainable Cities and Society, vol. 50, 2019


Clustering
----------

Clustering feature allows the users to improve the optimization speed by specifying a set of dates which could be considered
representative of the whole year (or the entire duration of the analysis). For example: four typical days could be selected
, one representing each season, and optihood would then provide the optimal design plan of the energy network based on these
days. Since the time resolution of the optimization problem would be much lower than simulating the whole year, the speed
of optimization is much faster when clustering is used.

Any clustering method (for example K-means clustering) can be chosen by the user and the results could be fed to optihood
for faster optimization. Note that in optihood one could use the results from clustering (which is to be done independently)
but the implementation of the clustering method itself is not a part of the optihood framework. The following results are
required from the clustering algorithm:

- Number of clusters
- Days of year representing each cluster
- Number of days in each cluster

In order to use the clustering feature, first a dictionary containing one item for each cluster, where keys and values are
the cluster's representative date and number of days, respectively, should be defined::

    cluster = {"2018-07-30": 26,
               "2018-02-03": 44,
               "2018-07-23": 32,
               "2018-09-18": 28,
               "2018-04-15": 22,
               "2018-10-01": 32,
               "2018-11-04": 32,
               "2018-10-11": 37,
               "2018-01-24": 15,
               "2018-08-18": 26,
               "2018-05-28": 23,
               "2018-02-06": 48}

Here, the days of the year have been represented using 12 clusters, where the first cluster consists of 26 days and is
represented by the date 30 June 2018.

This dictionary should be passed in the ``setFromExcel`` and ``optimize`` functions of the EnergyNetwork class::

    # set a time period for the optimization problem according to the number of clusers
    network = EnergyNetwork(pd.date_range("2018-01-01 00:00:00", "2018-01-12 23:00:00", freq="60min"), temperatureSH, temperatureDHW)

    # pass the dictionary defining the clusters to setFromExcel function
    network.setFromExcel("scenario.xls", numberOfBuildings=4, clusterSize=cluster, opt="costs")

    # pass the dictionary defining the clusters to optimize function
    envImpact, capacitiesTransformers, capacitiesStorages = network.optimize(solver='gurobi', clusterSize=cluster)

Note that the time period would need to be adjusted to include the timesteps corresponding to 12 days (12 x 24 = 288 timesteps
if hourly resolution is considered). Try the example on `selective days clustering <https://github.com/SPF-OST/optihood/blob/main/data/examples/selective_days_clustering.py>`_.
for a better grasp.