# Procedural Animated Camera

Press "N" in Viewport and find AN Tab ->

USAGE: Select a Collection with a bunch of Meshobjects. AN will pick up all the vertices your Collection is made of. To lower the amount
of vertices to look on there are Settings for "Mesh Every Nth Step" and Crop from Top and Bottom to reduce the vertices count
WARNING! if you have a huge model in your Collection with a lot of vertices Animationnodes will become sluggish every frame. Therefor
go into the Animationnodestree and search for the red box saying "SET CACHE TO "ONE TIME" if sluggish" - and do so, your cameramovements
will be smoother and the workload for your Cpu much less.

Procedural Camera Settings :
Animationnodes will create a bunch of different cameramovements depending on the styles (Dolly, Circle, Pan, Elevator) you want, and with the length you specify
- Camera : Specify your Camera
- Focus : Specify your Focus Empty (make sure that your Camera has a "track to" constrain with the empty as the target)
- Collection : Put the Object/s that is/are of interest in a collection and specify it here
- Seed : change value and all the camerapaths will change
- Vis Focus Points : when enabled shows all the points of your mesh of interest specified in "Collection"
- Mesh Every Nth Step : higher values mean less calculation - if you have a 3dscan that has loads of points this setting will only take every nth point into consideration
- Crop Vis Points from Start : reduces the focuspoints starting from the top (have "Vis Focus Points" enabled)
- Crop Vis Points from Bottom : reduces the focuspoints from bottom (have "Vis Focus Points" enabled)
- Animation Length : every cameramovement will have this length, if scenelength is longer there will be a bunch of cameramoves
- Dolly : specify if you want that cameramovement to be included
- Circle : specify if you want that cameramovement to be included
- Pan : specify if you want that cameramovement to be included
- Elevator : specify if you want that cameramovement to be included
- Center/ Focus depending on Cam Distance : if camera is far away it will not target the focus but the objects mean center, and vice versa, makes for better images as object is in center - the transistion will be linear/seamless
- Wiggle Focus Range : How much the focus is allowed to travel in x,y,z
- Wiggle Focus Speed : How fast the focus wiggles
        
Dolly Settings :
Animationnodes creates a line from the focus points to some random procedural point to act as a cam-path 
Animationnodes will pick a random value between the min and max for every cam-path of the same type - if you want to be specific make min and max equal
- Distance Min : this is the minimum distance from the focus to the object   
- Distance Max : this is the maximum distance from the focus to the object   
- Height Max : AN will pick a Z-starting value between 0 and this Setting
- Offset Endpoint 0-1 1=no motion : the line always connects to the focus some dolly-cam-movements may penetrate the object - this setting prevents this - putting in "1" results in no movement as the line becomes a point
    
Circle Motion Settings : 
Animationnodes creates a circle around the object/s for every Animationlength - these circles are different depending on the values below
Animationnodes will pick a random value between the min and max for every cam-path of the same type - if you want to be specific make min and max equal
- Circle Distance Min : the minimum cameracircle size
- Circle Distance Max : the maximum cameracircle size
- Circle segment Min 0-1 : the minimum circle-segment size (how much of the circle is used as a camera-path)
- Circle segment Max 0-1 : the maximum circle-segment size (how much of the circle is used as a camera-path)
- Circle min Height : the min z-value of the circle
- Circle max Height : the max z-value of the circle
        
Panmotion Settings :
Animationnodes will create a line perpendicular to the face the focus object is on
Animationnodes will pick a random value between the min and max for every cam-path of the same type - if you want to be specific make min and max equal
- Min Distance : minimum distance of the middle of the pan-path from the focusobject
- Max Distance : maximum distance of the middle of the pan-path from the focusobject
- Min Pan Path Length : minimum length of the camera-path 
- Max Pan Path Length : maximum length of the camera-path
    
Elevator Settings :
Animationnodes creates a point in a min-max Distance from the focus and generates a path from min-Z to max-Z to work as the camerapath
Animationnodes will pick a random value between the min and max for every cam-path of the same type - if you want to be specific make min and max equal
- Elevator Distance Min : minimum distance from focuspoint
- Elevator Distance Max : maximum distance from focuspoint
- Elevator Height Min : the minimum elevator height of the camera-path
- Elevator Height Max : the maximum elevator height of the camera-path

Author : faaaaarck

created with Blender 2.83.6 and Animation Nodes 2.1.7 on windows 10

![Image preview](https://github.com/samytichadou/animation_nodes_examples/blob/master/library/Utility/Procedural%20Animated%20Camera/image_preview.png)

<!---[Video preview](https://youtu.be/FxMaA0sqnoU?list=PL57BAmPXpXuOLKN-CjVJPmWcsqEqg7Fku)-->

[Blend file](https://github.com/samytichadou/animation_nodes_examples/blob/master/library/Utility/Procedural%20Animated%20Camera/Procedural%20Animated%20Camera.blend?raw=true)