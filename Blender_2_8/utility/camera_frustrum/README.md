# Camera_frustrum

This nodetree is a simple camera frustrum utility.
It checks for every vertex of objects in collections, if one of them is in the camera field of view, the object visibility is toggled on, otherwise, it is toggled off.

To use this
- Set the Camera Frustrum subprogram node settings (single collection or collection list, threshold and camera to use
- If you use it to render a still image, don't activate the Auto Execution on the node, instead, just execute the nodetree when your camera is setup
- If you use it to render animation, you can either activate Auto Execution, or Bake to Keyframes (this is the better solution with large scenes)

Optionaly, you can chose other actions to do when an object is in the camera field. Change it in the Action red frame of the nodetree

Cheers

tonton (Samy Tichadou)

created with Blender 2.80 and Animation Nodes 2.1.4 on windows 10

![camera_frustrum preview](https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/utility/camera_frustrum/AN_EXAMPLE_camera_frustrum_preview.png)

[Video preview](https://youtu.be/YrVsBZghcWI?list=PL57BAmPXpXuOLKN-CjVJPmWcsqEqg7Fku)

[Blend file](https://github.com/samytichadou/animation_nodes_examples/blob/master/Blender_2_8/utility/camera_frustrum/AN_EXAMPLE_camera_frustrum.blend?raw=true)