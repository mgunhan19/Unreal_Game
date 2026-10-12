import unreal

def spawn_3d_sphere(location=(0.0, 0.0, 100.0), scale=(1.0, 1.0, 1.0), label="Sphere_3D"):
    """
    Spawns a 3D Sphere StaticMeshActor in the currently active Unreal Editor level.
    """
    mesh_path = "/Engine/BasicShapes/Sphere.Sphere"
    sphere_mesh = unreal.EditorAssetLibrary.load_asset(mesh_path)
    if not sphere_mesh:
        mesh_path = "/Engine/BasicShapes/Sphere"
        sphere_mesh = unreal.EditorAssetLibrary.load_asset(mesh_path)
    
    if not sphere_mesh:
        unreal.log_error(f"[SpawnSphere] Küre static mesh bulunamadı: {mesh_path}")
        return None
    
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    if not actor_subsystem:
        unreal.log_error("[SpawnSphere] EditorActorSubsystem alınamadı.")
        return None
        
    spawn_loc = unreal.Vector(location[0], location[1], location[2])
    spawn_rot = unreal.Rotator(0.0, 0.0, 0.0)
    
    # StaticMeshActor olarak sahneye yerleştir
    actor = actor_subsystem.spawn_actor_from_object(sphere_mesh, spawn_loc, spawn_rot)
    if not actor:
        actor = actor_subsystem.spawn_actor_from_class(unreal.StaticMeshActor, spawn_loc, spawn_rot)
        if actor and hasattr(actor, 'static_mesh_component'):
            actor.static_mesh_component.set_static_mesh(sphere_mesh)
            
    if actor:
        actor.set_actor_label(label)
        actor.set_actor_scale3d(unreal.Vector(scale[0], scale[1], scale[2]))
        unreal.log(f"[SpawnSphere] Sahneye 3D Küre başarıyla eklendi! İsim: {actor.get_name()}, Etiket: {label}, Konum: {spawn_loc}")
        return actor
    else:
        unreal.log_error("[SpawnSphere] Küre aktörü sahneye eklenemedi.")
        return None

if __name__ == "__main__" or __name__ == "builtins":
    spawn_3d_sphere()
