# procedural_twisted_torus

This nodetree is a motion design preset based on a cinema 4d tutorial :
https://www.youtube.com/watch?v=7FdoEt9arIk&list=PL57BAmPXpXuPldSjGCUkHY6QAT6Zn6cd7&index=11&t=0s

It works by creating a simple circle matrix, and rotate incrementally its points through a subprogram.
After that, a grid matrix is distributed on top of these points.
Rotation of the points from first circle is controlled by time info node.
Sprite objects are then replicated through this resulting matrix.
Additionnaly, a scale effect is applied to sprites to make them bigger when they are far from the middle of the torus.
The entire object follows a controller object.

To use this, 
- set the sprite object and in Inputs category
- set the twist of the circle points in Inputs category
- set the base circle parameters in Inputs category
- set the Animation speed in Inputs category
- set the scale of duplicated objects in the Inputs category
- set the Sprite grid parameters in Inputs category
- toggle Scale effect On/Off and its Max Scale in Inputs category
- set the speed of the animation (noise is driven by time) in the Inputs category
- set the Matrix scale, Sprite rotation and scale in Inputs category
- set the Torus controller in Inputs category

You can optionnially check with the Viewers the appearance of your original circle, sprite grid, and the resulting Torus, but careful, this will not be rendered.

Careful, a custom trigger is set for updating the nodetree when Controller object changed (T-bar, Auto Execution panel)

Cheers

tonton (Samy Tichadou)

created with Blender 2.80 and Animation Nodes 2.1.4 on windows 10

![abstract_wave_instance_noise preview](https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/motion_design/twisted_torus_procedural/AN_EXAMPLE_abstract_twisted_torus_procedural_preview.png)

Video preview
https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/motion_design/twisted_torus_procedural/AN_EXAMPLE_abstract_twisted_torus_procedural_video.mp4

Blend file
https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/motion_design/twisted_torus_procedural/AN_EXAMPLE_abstract_twisted_torus_procedural.blend
