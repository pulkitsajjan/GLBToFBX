import bpy
import os

# Set the input and output directories
input_dir = "C:/Users/HI/Documents/GLB"
output_dir = "C:/Users/HI/Documents/FBX"


# Get a list of all GLB files in the input directory
glb_files = [f for f in os.listdir(input_dir) if f.endswith('.glb')]

# Iterate through each GLB file
for glb_file in glb_files:
    # Construct the input and output file paths
    input_path = os.path.join(input_dir, glb_file)
    output_path = os.path.join(output_dir, os.path.splitext(glb_file)[0] + '.fbx')
    
    # Load the GLB file into Blender
    bpy.ops.import_scene.gltf(filepath=input_path)

    # Create a folder for unpacked resources
    unpacked_resources_dir = os.path.join(input_dir, os.path.splitext(glb_file)[0])
    os.makedirs(unpacked_resources_dir, exist_ok=True)
    
    # Save the current temporary directory
    temp_dir = bpy.context.preferences.filepaths.temporary_directory
    
    # Set the temporary directory to the unpacked resources directory
    bpy.context.preferences.filepaths.temporary_directory = unpacked_resources_dir
    
    # Unpack resources
    bpy.ops.file.unpack_all(method='USE_LOCAL')
    
    # Restore the temporary directory
    bpy.context.preferences.filepaths.temporary_directory = temp_dir

    bpy.ops.export_scene.fbx(
        filepath=output_path,
        check_existing=False,
        filter_glob="*.fbx",
        use_selection=False,
        use_active_collection=False,
        global_scale=1.0,
        apply_unit_scale=True,
        apply_scale_options="FBX_SCALE_UNITS",
        bake_space_transform=False,
        object_types={"MESH", "ARMATURE"},
        use_mesh_modifiers=True,
        use_mesh_modifiers_render=True,
        mesh_smooth_type="OFF",
        use_subsurf=False,
        use_mesh_edges=False,
        use_tspace=False,
        use_custom_props=False,
        add_leaf_bones=True,
        primary_bone_axis="Y",
        secondary_bone_axis="X",
        use_armature_deform_only=False,
        armature_nodetype="NULL",
        bake_anim=False,
        bake_anim_use_all_bones=False,
        bake_anim_use_nla_strips=False,
        bake_anim_use_all_actions=False,
        bake_anim_force_startend_keying=True,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=1.0,
        path_mode="COPY",
        embed_textures=True,
        batch_mode="OFF",
        use_batch_own_dir=True,
        use_metadata=True,
    )
    
    # Remove all objects from the scene to prepare for the next import
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()
