import pytest
from vdf_parser import VDF


def test_parse_simple():
    vdf_text = '''
    "root"
    {
        "key1"  "value1"
        "key2"  "value2"
    }
    '''

    expected = {
        "root":{
            "key1":"value1",
            "key2":"value2"
        }
    }
    result = VDF().parseVdf(vdf_text)
    assert result==expected

def test_parse_complex():
    #file snippet taken from https://raw.githubusercontent.com/dotabuff/d2vpkr/master/dota/scripts/npc/npc_heroes.txt
    vdf_text = '''
    // Dota Heroes File
    "DOTAHeroes"	"1"
    {
        "Version"		"1"
        //=================================================================================================================
        // HERO: Base
        // Note: This is loaded and overriden/added to by values in the specific heroes chunks.
        //=================================================================================================================

        "npc_dota_hero_mirana"
        {
            "Model"		"models/heroes/mirana/mirana.vmdl"
            "IdleExpression"		"scenes/mirana/mirana_exp_idle_01.vcd"
            "SoundSet"		"Hero_Mirana"
            "PickSound"		"mirana_mir_spawn_01"
            "BanSound"		"mirana_mir_anger_01"
            "Enabled"		"1"
            "HeroUnlockOrder"		"1"
            "Role"			"Carry,Support,Escape,Nuker,Disabler"
            "Rolelevels"	"1,1,2,1,1"
            "Complexity"	"2"
            "Team"		"Good"
            "HeroID"		"9"
            "HeroOrderID"	"10"
            "ModelScale"		"0.790000"
            "VersusScale"		"0.790000"
            "SpectatorLoadoutScale" "0.9"
            "HeroGlowColor"		"220 194 248"
            "CMEnabled"		"1"
            "workshop_guide_name"		"Mirana"
            "LastHitChallengeRival"		"npc_dota_hero_luna"
            "HeroSelectSoundEffect"		"Hero_Mirana.Pick"
            "GibType"		"default"
            "ArmorPhysical"		"-2"
            "new_player_enable"		"1"
            "SimilarHeroes"	"21,14,123"
            "Adjectives"
            {
                "Steed"			"1"
                "Female"		"1"
            }
            "NameAliases"	"Princess;Moon;potm"
            "Ability1"		"mirana_starfall"
            "Ability2"		"mirana_arrow"
            "Ability3"		"mirana_leap"
            "Ability4"		"mirana_selemenes_faithful"
            "Ability5"		"generic_hidden"
            "Ability6"		"generic_hidden"

            "AbilityDraftAbilities"
            {
                "Ability1"		"mirana_starfall"
                "Ability2"		"mirana_arrow"
                "Ability3"		"mirana_leap"
                "Ability6"		"mirana_invis"
            }

            "Ability10"		"special_bonus_unique_mirana_3"
            "Ability11"		"special_bonus_unique_mirana_6"
            "Ability12"		"special_bonus_unique_mirana_5"
            "Ability13"		"special_bonus_unique_mirana_1"
            "Ability14"		"special_bonus_unique_mirana_4"
            "Ability15"		"special_bonus_20_crit_2"
            "Ability16"		"special_bonus_unique_mirana_2"
            "Ability17"		"special_bonus_unique_mirana_7"
            "Facets"
            {
                "mirana_moonlight"
                {
                    "Icon"				"moon"
                    "Color"				"Blue"
                    "GradientID"		"1"

                    "Abilities"
                    {
                        "Ability1"
                        {
                            "AbilityName"	"mirana_invis"
                            "AbilityIndex"	"5"
                            "AutoLevelAbility"	"false"
                        }
                    }
                }

                "mirana_sunlight"
                {
                    "Icon"				"sun"
                    "Color"				"Gray"
                    "GradientID"		"3"

                    "Abilities"
                    {
                        "Ability1"
                        {
                            "AbilityName"	"mirana_solar_flare"
                            "AbilityIndex"	"5"
                            "AutoLevelAbility"	"false"
                        }
                    }
                }
            }

            "AttackCapabilities"		"DOTA_UNIT_CAP_RANGED_ATTACK"
            "AttackDamageMin"		"-2"
            "AttackDamageMax"		"2"
            "AttackRate"		"1.700000"
            "BaseAttackSpeed"		"100"
            "AttackAnimationPoint"		"0.350000"
            "AttackAcquisitionRange"		"800"
            "AttackRange"		"630"
            "ProjectileModel"		"particles/units/heroes/hero_mirana/mirana_base_attack.vpcf"
            "ProjectileSpeed"		"900"
            "AttributePrimary"		"DOTA_ATTRIBUTE_ALL"
            "AttributeBaseStrength"		"18"
            "AttributeStrengthGain"		"1.9"
            "AttributeBaseIntelligence"		"22"
            "AttributeIntelligenceGain"		"1.4"
            "AttributeBaseAgility"		"26"
            "AttributeAgilityGain"		"2.5"
            "StatusManaRegen"	"0.4"
            "MovementSpeed"		"285"
            "HasAggressiveStance"		"1"
            "BoundsHullName"		"DOTA_HULL_SIZE_HERO"
            "particle_folder"		"particles/units/heroes/hero_mirana"
            "GameSoundsFile"		"soundevents/game_sounds_heroes/game_sounds_mirana.vsndevts"
            "VoiceFile"		"soundevents/voscripts/game_sounds_vo_mirana.vsndevts"
            "AbilityPreview"
            {
                "resource"		"resource/UI/Heroes/default.res"
                "movie"		"media/heroes/default"
                "resource"		"resource/UI/Heroes/default.res"
                "resource"		"resource/UI/Heroes/default.res"
                "resource"		"resource/UI/Heroes/default.res"
                "resource"		"resource/UI/Heroes/default.res"
            }
            "RenderablePortrait"
            {
                "Particles"
                {
                    "particles/units/heroes/hero_mirana/mirana_loadout.vpcf"		"loadout"
                }
            }
            "ItemSlots"
            {
                "0"
                {
                    "SlotIndex"		"0"
                    "SlotName"		"weapon"
                    "SlotText"		"#LoadoutSlot_Weapon"
                    "TextureWidth"		"256"
                    "TextureHeight"		"256"
                    "MaxPolygonsLOD0"		"2500"
                    "MaxPolygonsLOD1"		"1000"
                }
                "1"
                {
                    "SlotIndex"		"1"
                    "SlotName"		"head"
                    "SlotText"		"#LoadoutSlot_Head_Accessory"
                    "TextureWidth"		"512"
                    "TextureHeight"		"512"
                    "MaxPolygonsLOD0"		"3000"
                    "MaxPolygonsLOD1"		"1200"
                }
                "2"
                {
                    "SlotIndex"		"2"
                    "SlotName"		"arms"
                    "SlotText"		"#LoadoutSlot_Arms"
                    "TextureWidth"		"256"
                    "TextureHeight"		"256"
                    "MaxPolygonsLOD0"		"1500"
                    "MaxPolygonsLOD1"		"600"
                }
                "3"
                {
                    "SlotIndex"		"3"
                    "SlotName"		"back"
                    "SlotText"		"#LoadoutSlot_Back"
                    "TextureWidth"		"256"
                    "TextureHeight"		"256"
                    "MaxPolygonsLOD0"		"2000"
                    "MaxPolygonsLOD1"		"800"
                }
                "4"
                {
                    "SlotIndex"		"4"
                    "SlotName"		"shoulder"
                    "SlotText"		"#LoadoutSlot_Shoulder"
                    "TextureWidth"		"256"
                    "TextureHeight"		"256"
                    "MaxPolygonsLOD0"		"2000"
                    "MaxPolygonsLOD1"		"800"
                }
                "5"
                {
                    "SlotIndex"		"5"
                    "SlotName"		"mount"
                    "SlotText"		"#LoadoutSlot_Mount"
                    "TextureWidth"		"512"
                    "TextureHeight"		"512"
                    "MaxPolygonsLOD0"		"6000"
                    "MaxPolygonsLOD1"		"2400"
                }
                "6"
                {
                    "SlotIndex"		"6"
                    "SlotName"		"misc"
                    "SlotText"		"#LoadoutSlot_Quiver"
                    "TextureWidth"		"256"
                    "TextureHeight"		"256"
                    "MaxPolygonsLOD0"		"1000"
                    "MaxPolygonsLOD1"		"400"
                }
                "7"
                {
                    "SlotIndex"		"7"
                    "SlotName"		"taunt"
                    "SlotText"		"#LoadoutSlot_Taunt"
                }
                "8"
                {
                    "SlotIndex"		"8"
                    "SlotName"		"weapon_persona_1"
                    "SlotText"		"#LoadoutSlot_Weapon"
                    //"TextureWidth"		"256"
                    //"TextureHeight"		"256"
                    //"MaxPolygonsLOD0"		"800"
                    //"MaxPolygonsLOD1"		"600"
                }
                "9"
                {
                    "SlotIndex"		"9"
                    "SlotName"		"head_persona_1"
                    "SlotText"		"#LoadoutSlot_Head"
                    //"TextureWidth"		"256"
                    //"TextureHeight"		"256"
                    //"MaxPolygonsLOD0"		"1000"
                    //"MaxPolygonsLOD1"		"500"
                }
                "10"
                {
                    "SlotIndex"		"10"
                    "SlotName"		"armor_persona_1"
                    "SlotText"		"#LoadoutSlot_Armor"
                    //"TextureWidth"		"256"
                    //"TextureHeight"		"256"
                    //"MaxPolygonsLOD0"		"650"
                    //"MaxPolygonsLOD1"		"650"
                }
                "11"
                {
                    "SlotIndex"		"11"
                    "SlotName"		"back_persona_1"
                    "SlotText"		"#LoadoutSlot_Back"
                    //"TextureWidth"		"256"
                    //"TextureHeight"		"256"
                    //"MaxPolygonsLOD0"		"2500"
                    //"MaxPolygonsLOD1"		"1000"
                }
                "12"
                {
                    "SlotIndex"		"12"
                    "SlotName"		"mount_persona_1"
                    "SlotText"		"#LoadoutSlot_Mount"
                    //"TextureWidth"		"512"
                    //"TextureHeight"		"512"
                    //"MaxPolygonsLOD0"		"6000"
                    //"MaxPolygonsLOD1"		"2400"
                }
                "13"
                {
                    "SlotIndex"		"13"
                    "SlotName"		"taunt_persona_1"
                    "SlotText"		"#LoadoutSlot_Taunt"
                }
                "14"
                {
                    "SlotIndex" "14"
                    "SlotName" "ability_effects_1"
                    "SlotText" "mirana_starfall"
                    "DisplayInLoadout" "0"
                }
                "15"
                {
                    "SlotIndex" "15"
                    "SlotName" "ability_effects_2"
                    "SlotText" "mirana_arrow"
                    "DisplayInLoadout" "0"
                }
                "16"
                {
                    "SlotIndex" "16"
                    "SlotName" "ability_effects_3"
                    "SlotText" "mirana_leap"
                    "DisplayInLoadout" "0"
                }
                "17"
                {
                    "SlotIndex" "17"
                    "SlotName" "ability_effects_4"
                    "SlotText" "mirana_invis"
                    "DisplayInLoadout" "0"
                }
                // NOTE: persona_selector should be after persona item slots, so that those item slots can override its asset modifiers. See CEconItemView::CacheAssetModifiers
                "18"
                {
                    "SlotIndex"		"18"
                    "SlotName"		"persona_selector"
                    "SlotText"		"#LoadoutSlot_Persona_Selector"
                }
                "19"
                {
                    "SlotIndex"		"19"
                    "SlotName"		"hero_effigy"
                    "SlotText"		"#LoadoutSlot_HeroEffigy"
                }
                "20"
                {
                    "SlotIndex"		"20"
                    "SlotName"		"hero_effigy_persona_1"
                    "SlotText"		"#LoadoutSlot_HeroEffigy"
                }		}
            "Bot"
            {
                "Loadout"
                {
                    "item_tango"		"ITEM_CONSUMABLE | ITEM_SELLABLE"
                    "item_tango"		"ITEM_CONSUMABLE | ITEM_SELLABLE"
                    "item_branches"		"ITEM_CORE"
                    "item_branches"		"ITEM_CORE"
                    "item_magic_stick"		"ITEM_EXTENSION"
                    "item_boots"		"ITEM_CORE"
                    "item_bottle"		"ITEM_CORE | ITEM_SELLABLE"
                    "item_boots_of_elves"		"ITEM_EXTENSION"
                    "item_gloves"   		"ITEM_EXTENSION"
                    "item_power_treads"		"ITEM_DERIVED"
                    "item_recipe_magic_wand"		"ITEM_EXTENSION"
                    "item_magic_wand"		"ITEM_DERIVED | ITEM_SELLABLE"
                    "item_blade_of_alacrity"		"ITEM_EXTENSION"
                    "item_blade_of_alacrity"		"ITEM_EXTENSION"
                    "item_robe"		"ITEM_EXTENSION"
                    "item_recipe_diffusal_blade"		"ITEM_EXTENSION"
                    "item_diffusal_blade"		"ITEM_DERIVED"
                    "item_blade_of_alacrity"		"ITEM_EXTENSION"
                    "item_boots_of_elves"		"ITEM_EXTENSION"
                    "item_recipe_yasha"		"ITEM_EXTENSION"
                    "item_yasha"		"ITEM_DERIVED"
                    "item_blight_stone"		"ITEM_EXTENSION"
                    "item_mithril_hammer"		"ITEM_EXTENSION"
                    "item_mithril_hammer"		"ITEM_EXTENSION"
                    "item_desolator"		"ITEM_DERIVED"
                    "item_diadem"			"ITEM_EXTENSION"
                    "item_recipe_manta"			"ITEM_EXTENSION"
                    "item_manta"				"ITEM_LUXURY | ITEM_DERIVED"
                }
                "Build"
                {
                    "1"		"mirana_arrow"
                    "2"		"mirana_leap"
                    "3"		"mirana_starfall"
                    "4"		"mirana_starfall"
                    "5"		"mirana_starfall"
                    "6"		"mirana_invis"
                    "7"		"mirana_starfall"
                    "8"		"mirana_leap"
                    "9"		"mirana_leap"
                    "10"		"special_bonus_unique_mirana_3"
                    "11"		"mirana_leap"
                    "12"		"mirana_invis"
                    "13"		"mirana_arrow"
                    "14"		"mirana_arrow"
                    "15"		"special_bonus_unique_mirana_1"
                    "16"		"mirana_arrow"
                    "17"		""
                    "18"		"mirana_invis"
                    "19"		""
                    "20"		"special_bonus_20_crit_2"
                    "21"		""
                    "22"		""
                    "23"		""
                    "24"		""
                    "25"		"special_bonus_unique_mirana_2"
                }
                "HeroType"		"DOTA_BOT_GANKER | DOTA_BOT_SEMI_CARRY"
                "LaningInfo"
                {
                    "SoloDesire"		"1"
                    "RequiresBabysit"		"0"
                    "ProvidesBabysit"		"2"
                    "SurvivalRating"		"2"
                    "RequiresFarm"		"2"
                    "ProvidesSetup"		"1"
                    "RequiresSetup"		"1"
                }
            }
            "Persona"
            {
                "1"
                {
                    "name"					"npc_dota_hero_mirana_persona1"
                    "token"					"#npc_dota_hero_mirana_persona1"
                    "token_english"			"#npc_dota_hero_mirana_persona1__en"
                    "Model"					"models/heroes/mirana_persona/mirana_persona_base.vmdl"	// For tools only
                }
            }
            "MovementSpeedActivityModifiers"
            {
                "trot"		"0"
                "run"		"335"
            }
            "animation_transitions"
            {
                "ACT_DOTA_RUN"
                {
                    "regular"	"0.5"
                }
                "ACT_DOTA_IDLE"
                {
                    "regular"	"0.8"
                }
            }
            "precache"
            {
                "particle"			"particles/econ/events/anniversary_10th/anniversary_10th_hat_ambient_npc_dota_hero_mirana.vpcf"
                "particle"			"particles/econ/events/anniversary_10th/anniversary_10th_hat_ambient_npc_dota_hero_mirana_persona_1.vpcf"
            }
            "party_hat_effect"			"particles/econ/events/anniversary_10th/anniversary_10th_hat_ambient_npc_dota_hero_mirana.vpcf"
            "party_hat_effect_persona"	"particles/econ/events/anniversary_10th/anniversary_10th_hat_ambient_npc_dota_hero_mirana_persona_1.vpcf"
            "showcase_attachments"
            {
                "attach_hand1"		"1"
                "attach_hand2"		"2"
                "attach_head"		"3"
            }
        }
    }
    '''
    expected={'DOTAHeroes': '1', 'Version': '1', 'npc_dota_hero_mirana': {'Model': 'models/heroes/mirana/mirana.vmdl', 'IdleExpression': 'scenes/mirana/mirana_exp_idle_01.vcd', 'SoundSet': 'Hero_Mirana', 'PickSound': 'mirana_mir_spawn_01', 'BanSound': 'mirana_mir_anger_01', 'Enabled': '1', 'HeroUnlockOrder': '1', 'Role': 'Carry,Support,Escape,Nuker,Disabler', 'Rolelevels': '1,1,2,1,1', 'Complexity': '2', 'Team': 'Good', 'HeroID': '9', 'HeroOrderID': '10', 'ModelScale': '0.790000', 'VersusScale': '0.790000', 'SpectatorLoadoutScale': '0.9', 'HeroGlowColor': '220 194 248', 'CMEnabled': '1', 'workshop_guide_name': 'Mirana', 'LastHitChallengeRival': 'npc_dota_hero_luna', 'HeroSelectSoundEffect': 'Hero_Mirana.Pick', 'GibType': 'default', 'ArmorPhysical': '-2', 'new_player_enable': '1', 'SimilarHeroes': '21,14,123', 'Adjectives': {'Steed': '1', 'Female': '1'}, 'NameAliases': 'Princess;Moon;potm', 'Ability1': 'mirana_starfall', 'Ability2': 'mirana_arrow', 'Ability3': 'mirana_leap', 'Ability4': 'mirana_selemenes_faithful', 'Ability5': 'generic_hidden', 'Ability6': 'generic_hidden', 'AbilityDraftAbilities': {'Ability1': 'mirana_starfall', 'Ability2': 'mirana_arrow', 'Ability3': 'mirana_leap', 'Ability6': 'mirana_invis'}, 'Ability10': 'special_bonus_unique_mirana_3', 'Ability11': 'special_bonus_unique_mirana_6', 'Ability12': 'special_bonus_unique_mirana_5', 'Ability13': 'special_bonus_unique_mirana_1', 'Ability14': 'special_bonus_unique_mirana_4', 'Ability15': 'special_bonus_20_crit_2', 'Ability16': 'special_bonus_unique_mirana_2', 'Ability17': 'special_bonus_unique_mirana_7', 'Facets': {'mirana_moonlight': {'Icon': 'moon', 'Color': 'Blue', 'GradientID': '1', 'Abilities': {'Ability1': {'AbilityName': 'mirana_invis', 'AbilityIndex': '5', 'AutoLevelAbility': 'false'}}}, 'mirana_sunlight': {'Icon': 'sun', 'Color': 'Gray', 'GradientID': '3', 'Abilities': {'Ability1': {'AbilityName': 'mirana_solar_flare', 'AbilityIndex': '5', 'AutoLevelAbility': 'false'}}}}, 'AttackCapabilities': 'DOTA_UNIT_CAP_RANGED_ATTACK', 'AttackDamageMin': '-2', 'AttackDamageMax': '2', 'AttackRate': '1.700000', 'BaseAttackSpeed': '100', 'AttackAnimationPoint': '0.350000', 'AttackAcquisitionRange': '800', 'AttackRange': '630', 'ProjectileModel': 'particles/units/heroes/hero_mirana/mirana_base_attack.vpcf', 'ProjectileSpeed': '900', 'AttributePrimary': 'DOTA_ATTRIBUTE_ALL', 'AttributeBaseStrength': '18', 'AttributeStrengthGain': '1.9', 'AttributeBaseIntelligence': '22', 'AttributeIntelligenceGain': '1.4', 'AttributeBaseAgility': '26', 'AttributeAgilityGain': '2.5', 'StatusManaRegen': '0.4', 'MovementSpeed': '285', 'HasAggressiveStance': '1', 'BoundsHullName': 'DOTA_HULL_SIZE_HERO', 'particle_folder': 'particles/units/heroes/hero_mirana', 'GameSoundsFile': 'soundevents/game_sounds_heroes/game_sounds_mirana.vsndevts', 'VoiceFile': 'soundevents/voscripts/game_sounds_vo_mirana.vsndevts', 'AbilityPreview': {'resource': ['resource/UI/Heroes/default.res', 'resource/UI/Heroes/default.res', 'resource/UI/Heroes/default.res', 'resource/UI/Heroes/default.res', 'resource/UI/Heroes/default.res'], 'movie': 'media/heroes/default'}, 'RenderablePortrait': {'Particles': {'particles/units/heroes/hero_mirana/mirana_loadout.vpcf': 'loadout'}}, 'ItemSlots': {'0': {'SlotIndex': '0', 'SlotName': 'weapon', 'SlotText': '#LoadoutSlot_Weapon', 'TextureWidth': '256', 'TextureHeight': '256', 'MaxPolygonsLOD0': '2500', 'MaxPolygonsLOD1': '1000'}, '1': {'SlotIndex': '1', 'SlotName': 'head', 'SlotText': '#LoadoutSlot_Head_Accessory', 'TextureWidth': '512', 'TextureHeight': '512', 'MaxPolygonsLOD0': '3000', 'MaxPolygonsLOD1': '1200'}, '2': {'SlotIndex': '2', 'SlotName': 'arms', 'SlotText': '#LoadoutSlot_Arms', 'TextureWidth': '256', 'TextureHeight': '256', 'MaxPolygonsLOD0': '1500', 'MaxPolygonsLOD1': '600'}, '3': {'SlotIndex': '3', 'SlotName': 'back', 'SlotText': '#LoadoutSlot_Back', 'TextureWidth': '256', 'TextureHeight': '256', 'MaxPolygonsLOD0': '2000', 'MaxPolygonsLOD1': '800'}, '4': {'SlotIndex': '4', 'SlotName': 'shoulder', 'SlotText': '#LoadoutSlot_Shoulder', 'TextureWidth': '256', 'TextureHeight': '256', 'MaxPolygonsLOD0': '2000', 'MaxPolygonsLOD1': '800'}, '5': {'SlotIndex': '5', 'SlotName': 'mount', 'SlotText': '#LoadoutSlot_Mount', 'TextureWidth': '512', 'TextureHeight': '512', 'MaxPolygonsLOD0': '6000', 'MaxPolygonsLOD1': '2400'}, '6': {'SlotIndex': '6', 'SlotName': 'misc', 'SlotText': '#LoadoutSlot_Quiver', 'TextureWidth': '256', 'TextureHeight': '256', 'MaxPolygonsLOD0': '1000', 'MaxPolygonsLOD1': '400'}, '7': {'SlotIndex': '7', 'SlotName': 'taunt', 'SlotText': '#LoadoutSlot_Taunt'}, '8': {'SlotIndex': '8', 'SlotName': 'weapon_persona_1', 'SlotText': '#LoadoutSlot_Weapon'}, '9': {'SlotIndex': '9', 'SlotName': 'head_persona_1', 'SlotText': '#LoadoutSlot_Head'}, '10': {'SlotIndex': '10', 'SlotName': 'armor_persona_1', 'SlotText': '#LoadoutSlot_Armor'}, '11': {'SlotIndex': '11', 'SlotName': 'back_persona_1', 'SlotText': '#LoadoutSlot_Back'}, '12': {'SlotIndex': '12', 'SlotName': 'mount_persona_1', 'SlotText': '#LoadoutSlot_Mount'}, '13': {'SlotIndex': '13', 'SlotName': 'taunt_persona_1', 'SlotText': '#LoadoutSlot_Taunt'}, '14': {'SlotIndex': '14', 'SlotName': 'ability_effects_1', 'SlotText': 'mirana_starfall', 'DisplayInLoadout': '0'}, '15': {'SlotIndex': '15', 'SlotName': 'ability_effects_2', 'SlotText': 'mirana_arrow', 'DisplayInLoadout': '0'}, '16': {'SlotIndex': '16', 'SlotName': 'ability_effects_3', 'SlotText': 'mirana_leap', 'DisplayInLoadout': '0'}, '17': {'SlotIndex': '17', 'SlotName': 'ability_effects_4', 'SlotText': 'mirana_invis', 'DisplayInLoadout': '0'}, '18': {'SlotIndex': '18', 'SlotName': 'persona_selector', 'SlotText': '#LoadoutSlot_Persona_Selector'}, '19': {'SlotIndex': '19', 'SlotName': 'hero_effigy', 'SlotText': '#LoadoutSlot_HeroEffigy'}, '20': {'SlotIndex': '20', 'SlotName': 'hero_effigy_persona_1', 'SlotText': '#LoadoutSlot_HeroEffigy'}}, 'Bot': {'Loadout': {'item_tango': ['ITEM_CONSUMABLE | ITEM_SELLABLE', 'ITEM_CONSUMABLE | ITEM_SELLABLE'], 'item_branches': ['ITEM_CORE', 'ITEM_CORE'], 'item_magic_stick': 'ITEM_EXTENSION', 'item_boots': 'ITEM_CORE', 'item_bottle': 'ITEM_CORE | ITEM_SELLABLE', 'item_boots_of_elves': ['ITEM_EXTENSION', 'ITEM_EXTENSION'], 'item_gloves': 'ITEM_EXTENSION', 'item_power_treads': 'ITEM_DERIVED', 'item_recipe_magic_wand': 'ITEM_EXTENSION', 'item_magic_wand': 'ITEM_DERIVED | ITEM_SELLABLE', 'item_blade_of_alacrity': ['ITEM_EXTENSION', 'ITEM_EXTENSION', 'ITEM_EXTENSION'], 'item_robe': 'ITEM_EXTENSION', 'item_recipe_diffusal_blade': 'ITEM_EXTENSION', 'item_diffusal_blade': 'ITEM_DERIVED', 'item_recipe_yasha': 'ITEM_EXTENSION', 'item_yasha': 'ITEM_DERIVED', 'item_blight_stone': 'ITEM_EXTENSION', 'item_mithril_hammer': ['ITEM_EXTENSION', 'ITEM_EXTENSION'], 'item_desolator': 'ITEM_DERIVED', 'item_diadem': 'ITEM_EXTENSION', 'item_recipe_manta': 'ITEM_EXTENSION', 'item_manta': 'ITEM_LUXURY | ITEM_DERIVED'}, 'Build': {'1': 'mirana_arrow', '2': 'mirana_leap', '3': 'mirana_starfall', '4': 'mirana_starfall', '5': 'mirana_starfall', '6': 'mirana_invis', '7': 'mirana_starfall', '8': 'mirana_leap', '9': 'mirana_leap', '10': 'special_bonus_unique_mirana_3', '11': 'mirana_leap', '12': 'mirana_invis', '13': 'mirana_arrow', '14': 'mirana_arrow', '15': 'special_bonus_unique_mirana_1', '16': 'mirana_arrow', '17': '', '18': 'mirana_invis', '19': '', '20': 'special_bonus_20_crit_2', '21': '', '22': '', '23': '', '24': '', '25': 'special_bonus_unique_mirana_2'}, 'HeroType': 'DOTA_BOT_GANKER | DOTA_BOT_SEMI_CARRY', 'LaningInfo': {'SoloDesire': '1', 'RequiresBabysit': '0', 'ProvidesBabysit': '2', 'SurvivalRating': '2', 'RequiresFarm': '2', 'ProvidesSetup': '1', 'RequiresSetup': '1'}}, 'Persona': {'1': {'name': 'npc_dota_hero_mirana_persona1', 'token': '#npc_dota_hero_mirana_persona1', 'token_english': '#npc_dota_hero_mirana_persona1__en', 'Model': 'models/heroes/mirana_persona/mirana_persona_base.vmdl'}}, 'MovementSpeedActivityModifiers': {'trot': '0', 'run': '335'}, 'animation_transitions': {'ACT_DOTA_RUN': {'regular': '0.5'}, 'ACT_DOTA_IDLE': {'regular': '0.8'}}, 'precache': {'particle': ['particles/econ/events/anniversary_10th/anniversary_10th_hat_ambient_npc_dota_hero_mirana.vpcf', 'particles/econ/events/anniversary_10th/anniversary_10th_hat_ambient_npc_dota_hero_mirana_persona_1.vpcf']}, 'party_hat_effect': 'particles/econ/events/anniversary_10th/anniversary_10th_hat_ambient_npc_dota_hero_mirana.vpcf', 'party_hat_effect_persona': 'particles/econ/events/anniversary_10th/anniversary_10th_hat_ambient_npc_dota_hero_mirana_persona_1.vpcf', 'showcase_attachments': {'attach_hand1': '1', 'attach_hand2': '2', 'attach_head': '3'}}}
    vdf = VDF(options={"types":False})
    result =vdf.parseVdf(vdf_text)
    assert result==expected

def test_parse_types():
    vdf_text = '''
    "root"
    {
        "key1"  "1"
        "key2"  "true"
        "key3"  "1.1"
    }
    '''
    expected = {
        "root":{
            "key1":1,
            "key2":True,
            "key3":1.1
        }
    }
    result = VDF().parseVdf(vdf_text)
    assert result==expected

def test_parse_with_conditionals():
    vdf_text = '''
    "root"
    {
        "key1" "value1"
        "key2" "value2" [$DEBUG]
        "key3" "value3" [$LIVE]
    }
    '''
    vdf = VDF(options={"conditionals": ["LIVE"]}) #include LIVE remove others
    expected = {
        "root": {
            "key1": "value1",
            "key3": "value3"
        }
    }
    result = vdf.parseVdf(vdf_text)
    assert result == expected

def test_dump_simple():
    vdf_input = {
        "root":{
            "key1":"value1",
            "key2":"value2"
        }
    }
    expected= '''"root"\n{\n\t"key1"\t"value1"\n\t"key2"\t"value2"\n}\n'''
    result = VDF().dump(vdf_input)
    assert result==expected

