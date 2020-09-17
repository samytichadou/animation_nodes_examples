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
- set the sprite object and in Object Instancer (hide it if necessary from same node)
- set the divisions of Original Circle and Replicated Ones in Torus PreProcess Subprogram
- tweak the settings in Torus Creation Subprogram
- if needed, tweak the Scale Effect inside the Torus Creation Subprogram (point distance falloff node)

You can optionnially check with the Viewers (inside the Torus Creation Subprogram) the appearance of your original circle, sprite grid, and the resulting Torus, but careful, this will not be rendered.

Careful, a custom trigger is set for updating the nodetree when Controller object changed (T-bar, Auto Execution panel)

Cheers

tonton (Samy Tichadou)

created with Blender 2.83.5 and Animation Nodes 2.1.8 on windows 10

![abstract_wave_instance_noise preview](https://github.com/samytichadou/animation_nodes_examples/blob/master/library/Motion%20Design/Twisted%20Torus%20Procedural/image_preview.png)

[Video preview](https://youtu.be/jzHuaBHP058?list=PL57BAmPXpXuOLKN-CjVJPmWcsqEqg7Fku)

[Blend file](https://github.com/samytichadou/animation_nodes_examples/blob/master/library/Motion%20Design/Twisted%20Torus%20Procedural/Twisted%20Torus%20Procedural.blend?raw=true)
