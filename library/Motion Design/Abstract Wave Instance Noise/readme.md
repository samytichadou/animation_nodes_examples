# abstract_wave_instance_noise

This nodetree is a motion design preset based on a cinema 4d tutorial :
https://www.youtube.com/watch?v=xT-Wuqdtcjc&list=PL57BAmPXpXuPldSjGCUkHY6QAT6Zn6cd7&index=10&t=0s    

It allows to duplicate a sprite on a grid and move it through a falloff (noise falloff here, but you can use others)

To use this, 
- set the sprite object and its visibility
- set the Distribution Locations (grid as in the nodetree, could be anything else as long as it is a vector list)
- set the Scale of duplicated objects
- set the Speed of the animation (noise is driven by time)
- set the Effect Offset of the instances
- You can control the entire Effect with the Control vector
- set the Falloff in the subprogram if needed

You can optionnially check with the Viewers the appearance of your grid in the subprogram, but careful, this will not be rendered.

Cheers

tonton (Samy Tichadou)

created with Blender 2.83.3 and Animation Nodes 2.1.7 on windows 10

![abstract_wave_instance_noise preview](https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/motion_design/abstract_wave_instance_noise/AN_EXAMPLE_abstract_wave_instance_noise_preview.png)

[Video preview](https://youtu.be/t_uYw1zt6n0?list=PL57BAmPXpXuOLKN-CjVJPmWcsqEqg7Fku)

[Blend file](https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/motion_design/abstract_wave_instance_noise/AN_EXAMPLE_abstract_wave_instance_noise.blend?raw=true)
