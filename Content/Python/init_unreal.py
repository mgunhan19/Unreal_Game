import unreal
import os

print("[init_unreal] Game_new init_unreal.py başlatılıyor...")

def spawn_3d_sphere(location=(0.0, 0.0, 100.0), scale=(1.0, 1.0, 1.0), label="Sphere_3D"):
    """
    Mevcut Unreal Editor sahnesine bir 3D Küre (StaticMeshActor) ekler.
    """
    mesh_path = "/Engine/BasicShapes/Sphere.Sphere"
    sphere_mesh = unreal.EditorAssetLibrary.load_asset(mesh_path)
    if not sphere_mesh:
        mesh_path = "/Engine/BasicShapes/Sphere"
        sphere_mesh = unreal.EditorAssetLibrary.load_asset(mesh_path)
    
    if not sphere_mesh:
        unreal.log_error(f"[init_unreal] Küre static mesh bulunamadı: {mesh_path}")
        return None
    
    actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    if not actor_subsystem:
        unreal.log_error("[init_unreal] EditorActorSubsystem alınamadı.")
        return None
        
    spawn_loc = unreal.Vector(location[0], location[1], location[2])
    spawn_rot = unreal.Rotator(0.0, 0.0, 0.0)
    
    actor = actor_subsystem.spawn_actor_from_object(sphere_mesh, spawn_loc, spawn_rot)
    if not actor:
        actor = actor_subsystem.spawn_actor_from_class(unreal.StaticMeshActor, spawn_loc, spawn_rot)
        if actor and hasattr(actor, 'static_mesh_component'):
            actor.static_mesh_component.set_static_mesh(sphere_mesh)
            
    if actor:
        actor.set_actor_label(label)
        actor.set_actor_scale3d(unreal.Vector(scale[0], scale[1], scale[2]))
        unreal.log(f"[init_unreal] 3D Küre başarıyla sahneye eklendi! Aktör: {actor.get_name()}, Etiket: {label}, Konum: {spawn_loc}")
        return actor
    else:
        unreal.log_error("[init_unreal] Küre aktörü oluşturulamadı.")
        return None

# Sahneye küre ekle
spawn_3d_sphere()

# MCP Toolset kaydı (ToolsetRegistry aracılığıyla yapay zeka araçları)
try:
    import toolset_registry
    
    @unreal.uclass()
    class SceneTools(unreal.ToolsetDefinition):
        """Unreal Editor sahne ve aktör yönetim araçları."""
        
        @toolset_registry.tool_call
        @staticmethod
        def spawn_sphere(x: float = 0.0, y: float = 0.0, z: float = 100.0, scale: float = 1.0) -> str:
            """Mevcut sahneye 3D küre ekler.
            
            Args:
                x: X dünya koordinatı.
                y: Y dünya koordinatı.
                z: Z dünya koordinatı.
                scale: Küre ölçeği.
                
            Returns:
                İşlem sonucu mesajı.
            """
            actor = spawn_3d_sphere(location=(x, y, z), scale=(scale, scale, scale))
            if actor:
                return f"Başarıyla küre eklendi: {actor.get_actor_label()} @ ({x}, {y}, {z})"
            return "Küre eklenemedi."

        @toolset_registry.tool_call
        @staticmethod
        def execute_console_command(command: str) -> str:
            """Editor içerisinde bir konsol komutu çalıştırır.
            
            Args:
                command: Çalıştırılacak konsol komutu.
                
            Returns:
                Çalıştırma durumu.
            """
            unreal.SystemLibrary.execute_console_command(None, command)
            return f"Komut çalıştırıldı: {command}"

    unreal.ToolsetRegistry.register_toolset_class(SceneTools)
    unreal.log("[init_unreal] SceneTools ToolsetRegistry üzerine kaydedildi.")
except Exception as e:
    unreal.log_warning(f"[init_unreal] SceneTools Toolset kaydı atlandı: {e}")
