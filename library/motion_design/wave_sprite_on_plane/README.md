# wave_sprite_on_plane

This nodetree is a ready-to-use motion design effect based on a c4d tutorial :
https://www.youtube.com/watch?v=vlk33kbMHd8

A base plane object is "filled" by a bunch of sprite according to a parametric grid. Random rotation and scale are applied to them (Initial frame).
Then an empty sphere allows you to affect these sprites by moving/rotating/scaling them with a part of random (When affected frame).
A different vertex color is applied when sprites are affected by controller object. you can also use X location to determine which sprites have already been affected, and then keep the new vertex color. 
It allows for example to do some non-destructive text wave effects.

To use this, 
- set the division on the grid on X and Y in the Inputs category
- set a Base plane in the Inputs category
- set a Controller in the Inputs category
- set a Sprite in the Inputs category
- use the output to do some effects
- set the Initial category settings for repartition of the sprite
- set the When affected category settings for loc/rot/scale of the sprite when affected by the controller
- set the vertex color options in the Color controls category

You can optionnially check with the Viewers the appearance of your grid, but careful, this will not be rendered.

Cheers

tonton (Samy Tichadou)

created with Blender 2.80 and Animation Nodes 2.1.4 on windows 10

![wave_sprite_on_plane preview](https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/motion_design/wave_sprite_on_plane/AN_EXAMPLE_wave_sprite_on_plane_preview.png)

[Video preview](https://youtu.be/KF06_6Insnc?list=PL57BAmPXpXuOLKN-CjVJPmWcsqEqg7Fku)

[Blend file](https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/motion_design/wave_sprite_on_plane/AN_EXAMPLE_wave_sprite_on_plane.blend?raw=true)
