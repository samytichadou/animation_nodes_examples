# procedural_spring

This nodetree is a utility to quickly create a spring-type object.

It generates a circles and loop through every of its points to give them a Z offset, then apply the resulting spline to a curve object.Q

To use this,
- set the object input in procedural_spring group node
- set number of vertices, radius, number of segments, size, smoothing and bevel depth in procedural_spring group node
- set an output object for the resulting spring in procedural_spring group node (must be a curve object)

The generation being done in a subprogram group node, you can set several spring objects by duplicating procedural_spring group node and settings different output objects

Cheers

tonton (Samy Tichadou)

created with Blender 2.80 and Animation Nodes 2.1.4 on windows 10

![procedural_spring preview](https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/utility/procedural_spring/AN_EXAMPLE_procedura_spring_preview.png)

Video preview
https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/utility/procedural_spring/AN_EXAMPLE_procedura_spring_video.m4v?raw=true

Blend file
https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/utility/procedural_spring/AN_EXAMPLE_procedura_spring.blend?raw=true

