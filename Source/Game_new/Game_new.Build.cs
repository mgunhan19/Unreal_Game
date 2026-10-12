// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class Game_new : ModuleRules
{
	public Game_new(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

		PublicDependencyModuleNames.AddRange(new string[] {
			"Core",
			"CoreUObject",
			"Engine",
			"InputCore",
			"EnhancedInput",
			"AIModule",
			"StateTreeModule",
			"GameplayStateTreeModule",
			"UMG",
			"Slate"
		});

		PrivateDependencyModuleNames.AddRange(new string[] { });

		PublicIncludePaths.AddRange(new string[] {
			"Game_new",
			"Game_new/Variant_Platforming",
			"Game_new/Variant_Platforming/Animation",
			"Game_new/Variant_Combat",
			"Game_new/Variant_Combat/AI",
			"Game_new/Variant_Combat/Animation",
			"Game_new/Variant_Combat/Gameplay",
			"Game_new/Variant_Combat/Interfaces",
			"Game_new/Variant_Combat/UI",
			"Game_new/Variant_SideScrolling",
			"Game_new/Variant_SideScrolling/AI",
			"Game_new/Variant_SideScrolling/Gameplay",
			"Game_new/Variant_SideScrolling/Interfaces",
			"Game_new/Variant_SideScrolling/UI"
		});

		// Uncomment if you are using Slate UI
		// PrivateDependencyModuleNames.AddRange(new string[] { "Slate", "SlateCore" });

		// Uncomment if you are using online features
		// PrivateDependencyModuleNames.Add("OnlineSubsystem");

		// To include OnlineSubsystemSteam, add it to the plugins section in your uproject file with the Enabled attribute set to true
	}
}
