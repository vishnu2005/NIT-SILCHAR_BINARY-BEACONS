import bpy
import json

print("hello")




## Ensure the active object is the MB-Lab model
#obj = bpy.context.active_object

## Print object name to confirm selection
#print("Selected object:", obj.name)

## Print all attributes of the object
#print("Object attributes:")
#for attr in dir(obj):
#    print(attr)

## Print all custom properties of the object
#print("\nCustom properties:")
#for key in obj.keys():
#    print(key)
#    
## Print all attributes of the object's data
#print("\nObject data attributes:")
#for attr in dir(obj.data):
#    print(attr)

## Print all custom properties of the object's data
#print("\nCustom properties in data:")
#for key in obj.data.keys():
#    print(key)



# Function to import measurements from JSON file
def import_measurements(json_file_path):
    with open(json_file_path) as file:
        data = json.load(file)
    return data.get('measures', {})

# Function to update the MB-Lab model with the imported measurements
def update_model_with_measurements(measurements):
    available_keys = bpy.context.active_object.keys()
    print("Available keys in the MB-Lab model:", available_keys)
    
    for key, value in measurements.items():
        if key in available_keys:
            print(key)
            bpy.context.active_object[key] = value
#            bpy.data.objects["f_as01"].key = value

            print(f"Updated {key} to {value}")
        else:
            print(f"Measurement key '{key}' not found in MB-Lab model.")

# Path to your JSON file
json_file_path = 'C:/Users/DELL/Documents/C++/Hackerramp/NIT-SILCHAR_BINARY-BEACONS/user_measurements.json'

# Import the measurements from the JSON file
measurements = import_measurements('C:/Users/DELL/Documents/C++/Hackerramp/NIT-SILCHAR_BINARY-BEACONS/user_measurements.json')
print("Measurements imported:", measurements)

## Ensure that an MB-Lab character is selected
#if bpy.context.object in bpy.context.object.keys():
#    print("MB-Lab character selected.")
#    # Update the model with the imported measurements
update_model_with_measurements(measurements)
#    # Redraw the view to update the changes
bpy.context.view_layer.update()
print("Measurements updated successfully.")
#else:
#    print("No MB-Lab character selected. Please select an MB-Lab character.")

# Print all custom properties of the object
print("\nCustom properties:")
for key in bpy.context.active_object.keys():
    print(key,":",bpy.context.active_object[key])
    if key=='character_age':
        bpy.context.active_object[key]=0.4556577
        print("updated char mass")
        bpy.context.view_layer.update()
    else:
        continue
bpy.context.view_layer.update()

bpy.ops.export_scene.gltf(filepath="updated_model.glb")
    
# Ensure the active object is the MB-Lab model


## Print object name to confirm selection
#print("Selected object:", bpy.context.active_object.name)

## Print all custom properties of the object
#print("\nCustom properties of the object:")
#for key in bpy.context.active_object.keys():
#    print(key)

## Print all custom properties of the object's data
#print("\nCustom properties of the object's data:")
#for key in bpy.context.active_object.data.keys():
#    print(key)
