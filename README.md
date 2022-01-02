# Deforming graphs with verlet

An experiment in deforming graphs with the verlet algorithm. Still incomplete.

The motivating example for this was a maze represented as a graph. We have vertices V and edges E 
as well as an additional attribute of the vertices, their location in 2D space. Then we assign masses to them 
and progressively deform the graph to one that admits simpler policies for maze solving, e.g., just go to the next nearest
neighbor on your right until you reach the exit. 




