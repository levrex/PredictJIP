# Big joints in DAS28
L_Big_Joints_28 = [
    'Zwelling_pols L_positive', 'Zwelling_pols R_positive',
    'Zwelling_knie links_positive', 'Zwelling_knie rechts_positive',
    'Zwelling_schouder L_positive', 'Zwelling_schouder R_positive',
    'Zwelling_Elleboog L_positive', 'Zwelling_elleboog R_positive',
    
    'Pijn_pols L_positive', 'Pijn_pols R_positive',
    'Pijn_schouder L_positive', 'Pijn_schouder R_positive',
    'Pijn_Elleboog L_positive', 'Pijn_elleboog R_positive',
    'Pijn_knie links_positive', 'Pijn_knie rechts_positive',   
]
                 
# Heads up: We have no joints measured in the foot if we look at DAS28 joint scheme

# Joint involvmeent Foot (according to DAS44) = Only pip, mcp, IP and wrist
L_Hand_Tender_28 = [
    'Pijn_pip 2 links hand_positive', 'Pijn_pip 2 rechts hand_positive',
    'Pijn_pip 3 links hand_positive', 'Pijn_pip 3 rechts hand_positive',
    'Pijn_pip 4 links hand_positive', 'Pijn_pip 4 rechts hand_positive',
    'Pijn_pip 5 links hand_positive', 'Pijn_pip 5 rechts hand_positive',
    'Pijn_mcp 1 links_positive', 'Pijn_mcp 1 rechts_positive',
    'Pijn_mcp 2 links_positive', 'Pijn_mcp 2 rechts_positive',
    'Pijn_mcp 3 links_positive', 'Pijn_mcp 3 rechts_positive',
    'Pijn_mcp 4 links_positive', 'Pijn_mcp 4 rechts_positive',
    'Pijn_mcp 5 links_positive', 'Pijn_mcp 5 rechts_positive',
    'Pijn_IP links_positive', 'Pijn_IP rechts_positive'
]

L_Hand_Swelling_28 = [
    'Zwelling_pols L_positive', 'Zwelling_pols R_positive',
    'Zwelling_pip 2 links hand_positive', 'Zwelling_pip 2 rechts hand_positive',
    'Zwelling_pip 3 links hand_positive', 'Zwelling_pip 3 rechts hand_positive',
    'Zwelling_pip 4 links hand_positive', 'Zwelling_pip 4 rechts hand_positive',
    'Zwelling_pip 5 links hand_positive', 'Zwelling_pip 5 rechts hand_positive',
    'Zwelling_mcp 1 links_positive', 'Zwelling_mcp 1 rechts_positive',
    'Zwelling_mcp 2 links_positive', 'Zwelling_mcp 2 rechts_positive',
    'Zwelling_mcp 3 links_positive', 'Zwelling_mcp 3 rechts_positive',
    'Zwelling_mcp 4 links_positive', 'Zwelling_mcp 4 rechts_positive',
    'Zwelling_mcp 5 links_positive', 'Zwelling_mcp 5 rechts_positive',
    'Zwelling_IP links_positive', 'Zwelling_IP rechts_positive'
]

# Small joints in DAS28
L_Small_Joints_28 = [ # Same as l_DAS28_hand
    'Pijn_pip 2 links hand_positive', 'Pijn_pip 2 rechts hand_positive',
    'Pijn_pip 3 links hand_positive', 'Pijn_pip 3 rechts hand_positive',
    'Pijn_pip 4 links hand_positive', 'Pijn_pip 4 rechts hand_positive',
    'Pijn_pip 5 links hand_positive', 'Pijn_pip 5 rechts hand_positive',
    'Pijn_mcp 1 links_positive', 'Pijn_mcp 1 rechts_positive',
    'Pijn_mcp 2 links_positive', 'Pijn_mcp 2 rechts_positive',
    'Pijn_mcp 3 links_positive', 'Pijn_mcp 3 rechts_positive',
    'Pijn_mcp 4 links_positive', 'Pijn_mcp 4 rechts_positive',
    'Pijn_mcp 5 links_positive', 'Pijn_mcp 5 rechts_positive',
    'Pijn_IP links_positive', 'Pijn_IP rechts_positive',
    
    'Zwelling_pip 2 links hand_positive', 'Zwelling_pip 2 rechts hand_positive',
    'Zwelling_pip 3 links hand_positive', 'Zwelling_pip 3 rechts hand_positive',
    'Zwelling_pip 4 links hand_positive', 'Zwelling_pip 4 rechts hand_positive',
    'Zwelling_pip 5 links hand_positive', 'Zwelling_pip 5 rechts hand_positive',
    'Zwelling_mcp 1 links_positive', 'Zwelling_mcp 1 rechts_positive',
    'Zwelling_mcp 2 links_positive', 'Zwelling_mcp 2 rechts_positive',
    'Zwelling_mcp 3 links_positive', 'Zwelling_mcp 3 rechts_positive',
    'Zwelling_mcp 4 links_positive', 'Zwelling_mcp 4 rechts_positive',
    'Zwelling_mcp 5 links_positive', 'Zwelling_mcp 5 rechts_positive',
    
    'Zwelling_IP links_positive', 'Zwelling_IP rechts_positive'
]

 
# All joints for total DAS44 scheme
L_DAS_Joints_28 =  ['Pijn_pols L_positive', 'Pijn_pols R_positive',
    'Pijn_pip 2 links hand_positive', 'Pijn_pip 2 rechts hand_positive',
    'Pijn_pip 3 links hand_positive', 'Pijn_pip 3 rechts hand_positive',
    'Pijn_pip 4 links hand_positive', 'Pijn_pip 4 rechts hand_positive',
    'Pijn_pip 5 links hand_positive', 'Pijn_pip 5 rechts hand_positive',
    'Pijn_mcp 1 links_positive', 'Pijn_mcp 1 rechts_positive',
    'Pijn_mcp 2 links_positive', 'Pijn_mcp 2 rechts_positive',
    'Pijn_mcp 3 links_positive', 'Pijn_mcp 3 rechts_positive',
    'Pijn_mcp 4 links_positive', 'Pijn_mcp 4 rechts_positive',
    'Pijn_mcp 5 links_positive', 'Pijn_mcp 5 rechts_positive',
    'Pijn_IP links_positive', 'Pijn_IP rechts_positive',
    'Pijn_schouder L_positive', 'Pijn_schouder R_positive',
    'Pijn_Elleboog L_positive', 'Pijn_elleboog R_positive',
    'Pijn_knie links_positive', 'Pijn_knie rechts_positive',

    'Zwelling_pols L_positive', 'Zwelling_pols R_positive',
    'Zwelling_pip 2 links hand_positive', 'Zwelling_pip 2 rechts hand_positive',
    'Zwelling_pip 3 links hand_positive', 'Zwelling_pip 3 rechts hand_positive',
    'Zwelling_pip 4 links hand_positive', 'Zwelling_pip 4 rechts hand_positive',
    'Zwelling_pip 5 links hand_positive', 'Zwelling_pip 5 rechts hand_positive',
    'Zwelling_mcp 1 links_positive', 'Zwelling_mcp 1 rechts_positive',
    'Zwelling_mcp 2 links_positive', 'Zwelling_mcp 2 rechts_positive',
    'Zwelling_mcp 3 links_positive', 'Zwelling_mcp 3 rechts_positive',
    'Zwelling_mcp 4 links_positive', 'Zwelling_mcp 4 rechts_positive',
    'Zwelling_mcp 5 links_positive', 'Zwelling_mcp 5 rechts_positive',
    'Zwelling_knie links_positive', 'Zwelling_knie rechts_positive',
    'Zwelling_schouder L_positive', 'Zwelling_schouder R_positive',
    'Zwelling_Elleboog L_positive', 'Zwelling_elleboog R_positive',
    'Zwelling_IP links_positive', 'Zwelling_IP rechts_positive'
]
