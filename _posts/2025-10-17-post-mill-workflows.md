

```
markdown

title: "PCB Board"
date: 2025-10-30



## About

PCB board created using Maker Cam

## Milling Workflow

### Key Notes

- .8mm Corn flat-end bit is used to remove the bulk of the material
- The .2mm*30ºEngraving(Metal) engraving bit will be used to cut out the copper traces
- The Makera Milling machine affixes the FR4 using clamps, rather than adhesive, so tabs are necessary to keep the PCB in place
- 2D contour is used for edge cuts
- 2D pocket is used for copper traces
- 2D drilling is used for drill holes

## PCB Toolpath Workflow on MakeraCAM

1. Open MakeraCAM on your desktop.
2. Select the "3-AXIS" option on the welcome screen.
3. Edit the "Stock" settings in the top right corner
   - For Material, select "PCB"
   - For Length(X), adjust the value to 127mm
   - For Width(Y), adjust the value to 101mm
   - For Height(Z), adjust the value to 1.7mm (thickness of FR4)
4. In the top toolbar, click the icon titled "import PCB" and individually insert all Gerber files into the workspace.
5. The imported gerbers will likely populate outside of the workspace, so select all 2D layers, hover over the "Adjust object" and "Transform" drop-down menu and select the "Move" tool
   - When layers are dotted, that indicates that they are selected; when layers are solid, that indicates that they are unselected
6. Select the bottom left corner as the anchor point
7. Set both the X and Y location values to 6 mm, which positions the file in the bottom right corner of the workspace
8. Keeping all layers selected, hold the shift key and deselect the outer edge of the Edge_cuts
9. Toggle the visibility such that only the "F_Cu" and the "Edge_cuts" layer are visible
10. In the top toolbar, hover over the "2D Path" drop-down menu and select the "2D Pocket" option
11. In the dialogue box, adjust the "End Depth" value to .05mm
12. Under "Tools," click the "Add Tool" button, select ".8mm Corn tool" and click "Choose"
13. Click "Add Tool" again, select the ".2mm*30ºEngraving(Metal)," and click "Choose"
14. Ensure that the material selected is "PCB"
15. Click "Calculate"; you should see a "2D Pocket" toolpath fall under the Path dropdown in the hierarchy
16. If you have drill files, untoggle the visibility for all "F_Cu" and "Edge_cuts" layers and toggle visibility for all drill files
17. In the top toolbar, hover over the "2D Path" drop-down menu and select the "2D Drilling" option
18. In the dialogue box, adjust the "Drill Tip End Depth" value to 1.7mm
19. Under "Tools," click the "Add Tool" button, select ".8mm Corn tool" and click "Choose"
20. Click "Calculate"; you should see a "2D Drilling" toolpath fall under the Path dropdown in the hierarchy
21. To design a toolpath for the edge cuts, untoggle the visibility for all drill files and toggle visibility for solely the "Edge_cuts" layer
22. Select the inner outline of the "Edge_cuts" layer
23. In the top toolbar, hover over the "2D Path" drop-down menu and select the "2D Contour" option (synonymous with a "Pocket" cut)
24. In the dialogue box, adjust the "End Depth" value to 1.7mm
25. Under "Tools," click the "Add Tool" button, select ".8mm Corn tool" and click "Choose"
26. Under "Strategy," select "Outside"
27. Under "Tabs," select "Custom," and click "Add"
28. Add appropriate tabs around the selected "Edge_cuts" layer (typically, 3 will be sufficient)
   - **Tip:** Ensure that these tabs are staggered and not directly across from one another
29. Click "Calculate"; you should see a "2D Contour" toolpath fall under the Path dropdown in the hierarchy
30. In the top toolbar, click the icon "Preview Toolpaths," and select all toolpaths in the pop-up dialogue box
31. Click "Preview" and press the play button to view a simulation of the toolpaths
32. In the top toolbar, click the "Export" button, ensure all toolpaths are selected, and click "Export"
33. Rename the .nc file to your last name, your first initial, and your project name, followed by "gcode"

## PCB Milling on Carvera Controller

1. Open the Carvera Controller software on the desktop
2. In the top toolbar, click on the button with the status "N/A disconnected"
3. Select the appropriate COM port to connect the Carvera to the computer (if the COM port is already connected, leave it as is)
4. In the menu in the top right corner, click "Switch to display manual control interface" followed by the "Home" button
5. Under "Tool Status and Control," ensure that the probe is charged to at least 3.6V (this ensures the machine operates in the z-axis as intended)
6. In the bottom left corner, open the G-code from your files
7. Before starting the mill, open the menu in the top right corner and click the "Switch to display file preview interface" to preview the toolpaths
8. Click "Config and run," and ensure that both the "auto vacuum" and "auto leveling" options are on.
9. Once all settings are verified, click "Run"
```
## PCB Import and Setup

1. Open project 3-axis
2. File → Import PCB → select Edge Cuts.gbr file
3. File → Import PCB → select F.Cu layer to add top layer copper file
4. File → Import PCB → select Resistance1-PTH.drl (drill file) to mark where the CNC should drill holes into the board
5. Select board and press M, set the anchor to the bottom left corner and move board to (6, 6)
   - **Note:** If the object is dotted, it is selected. If it is solid, then it is not selected

## Configure 2D Pocket Toolpath

6. Go to top line, hit shift key and deselect the top line
7. Block the bottom three files
8. Select 2D Pocket to add a toolhead to the CNC
9. Set end depth to 0.05mm
10. Go to add tool → 0.8mm Corn
11. Go to add tool → 0.2mm*30 Engraving(Metal)
12. Select choose
13. Click calculate

## Configure 2D Drilling Toolpath

14. Block everything but the drl files
15. Select everything and select 2D drilling
16. Set drill tip end depth to 1.7mm
17. Just add the 0.8mm Corn tool
18. Calculate

## Configure 2D Contour Toolpath

19. Block everything but resistance edge cuts (Deselect top line and select bottom line)
20. 2D contour
21. End depth 1.7mm
22. Tool 0.8mm Corn
23. Strategy: position is outside
24. Go to tabs → Custom → tabs → add → click on selected box (you want 3 tabs)
   - **Note:** Don't put tabs across each other! It will break the board. Make sure to offset them slightly
25. Click preview at the top

