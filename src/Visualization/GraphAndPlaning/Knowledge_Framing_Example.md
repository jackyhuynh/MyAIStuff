Create a subdivision

Draw the following:

Top-level(0) = planned community - attributes = power/water/gas/internet/main roads

Next-Level down(1a) = sidewalks - attributes = made of concrete/connected to main roads

Next-Level down(1b) = subdivison - attributes = builder owned, connected by a road to main road

Next-level-down(2a) - subset(1b) = individual house - attributes = personal owner, connected to road by driveway, has a
lawn

Next-level-down(2b) - subset(1b) = playgrounds - attributes = connected to subdivision, fun, has a slide and swingset

Pseudocode:

property(power, planned community, T)\
property(water, planned community, T)\
property(gas, planned community, T)\
property(internet, planned community, T)\
property(main roads, planned community, T)

sidewalks C planned community\
subdivision C planned community

rel(sidewalks, subset, planned community)\
rel(subdivision, subset, planned community)

