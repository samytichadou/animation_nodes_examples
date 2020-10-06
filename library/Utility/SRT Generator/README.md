# SRT Generator
This Nodetree takes all Text Strips from a Scene Timeline and format them as a srt (subrip text) file in a Blender Text Block. User can then save this Text Block to use it in a classic media player.

To use it :
- Set the Text Output to target Text Block
- Set a Line Limit to split long texts
- Set Cut at Space if needed (if False, text split could happen in the middle of a word
- Set Include Muted Strips if needed
- Set specific Timeline Scene if needed

NB : The nodetree does not have Auto Execution On by default, user has to manually execute it to create the srt

Author : tonton (Samy Tichadou)

created with Blender 2.83.5 and Animation Nodes 2.1.8 on windows 10

![Image preview](https://github.com/samytichadou/animation_nodes_examples/blob/master/library/Utility/SRT%20Generator/image_preview.png)

<!---[Video preview](https://youtu.be/dzgT9opN3RM?list=PL57BAmPXpXuOLKN-CjVJPmWcsqEqg7Fku)-->

[Blend file](https://github.com/samytichadou/animation_nodes_examples/blob/master/library/Utility/SRT%20Generator/SRT%20Generator.blend?raw=true)