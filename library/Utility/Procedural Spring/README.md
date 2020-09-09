# Procedural Spring

This nodetree is a utility to quickly create a spring-type object.

It generates a circles and loop through every of its points to give them a Z offset, then apply the resulting spline to a curve object.Q

To use this,
- set the object input in Spring Creator Subprogram
- set number of vertices, radius, number of segments, size, smoothing, bevel depth and resolution in Spring Creator Subprogram
- set an output object for the resulting spring in Spring Creator Subprogram (must be a curve object)

The generation being done in a subprogram group node, you can set several spring objects by duplicating procedural_spring group node and settings different output objects

Cheers

tonton (Samy Tichadou)

created with Blender 2.83.3 and Animation Nodes 2.1.7 on Windows 10

![procedural_spring preview](https://github.com/samytichadou/animation_nodes_examples/blob/master/library/Utility/Procedural%20Spring/image_preview.png)

[Video preview](https://youtu.be/FxMaA0sqnoU?list=PL57BAmPXpXuOLKN-CjVJPmWcsqEqg7Fku)

[Blend file](https://github.com/samytichadou/animation_nodes_examples/blob/master/library/Utility/Procedural%20Spring/Procedural%20Spring.blend?raw=true)