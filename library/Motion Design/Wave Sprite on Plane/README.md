# wave_sprite_on_plane

This nodetree is a ready-to-use motion design effect based on a c4d tutorial :
https://www.youtube.com/watch?v=vlk33kbMHd8

A base plane object is "filled" by a bunch of sprite according to a parametric grid. Random rotation and scale are applied to them (Initial frame).
Then a Falloff allows you to affect these sprites by moving/rotating/scaling them with a part of random (When affected frame).
A different vertex color is applied when sprites are affected by another falloff.You can tweak it like in this case to keep the new vertex color. 
It allows for example to do some non-destructive text wave effects.

To use this, 
- set the division on the grid on X and Y in the Wave Preprocess Subprogram
- set a Base plane in the Wave Preprocess Subprogram
- set the object instancer (Deep Copy is needed if you want to affect the Vertex Colors)
- set the Falloffs
- set the "Initial" settings for repartition of the sprite in the Wave Creation Subprogram
- set the "Affected" settings for loc/rot/scale of the sprite when affected by the controller in the Wave Creation Subprogram
- set the vertex color options in the Wave Creation Subprogram

You can optionnially check with the Viewers the appearance of your grid, but careful, this will not be rendered.

A Custom Trigger is set for the controller object.

Cheers

tonton (Samy Tichadou)

created with Blender 2.83 and Animation Nodes 2.1.8 on windows 10

![wave_sprite_on_plane preview](https://github.com/samytichadou/animation_nodes_examples/blob/master/library/Motion%20Design/Wave%20Sprite%20on%20Plane/image_preview.png)

[Video preview](https://youtu.be/KF06_6Insnc?list=PL57BAmPXpXuOLKN-CjVJPmWcsqEqg7Fku)

[Blend file](https://github.com/samytichadou/animation_nodes_examples/blob/master/library/Motion%20Design/Wave%20Sprite%20on%20Plane/Wave%20Sprite%20on%20Plane.blend?raw=true)
