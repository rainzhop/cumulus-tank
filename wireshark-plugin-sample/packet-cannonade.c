#include "config.h"
#include <epan/packet.h>

#define CANNONADE_PORT 9933

static void dissect_cannonade(tvbuff_t *tvb, 
        packet_info *pinfo, proto_tree *tree);

static int proto_cannonade = -1;

static int hf_cannonade_id = -1;
static int hf_cannon_num = -1;
static int hf_cannon_fire = -1;
static int hf_cannon_fire_b[8] = {-1, -1, -1, -1, -1, -1, -1, -1};

static gint ett_cannonade = -1;

void proto_register_cannonade(void)
{
    static hf_register_info hf[] = {
        { &hf_cannonade_id, 
            { "CANNONADE Identifier",
            "cannonade.identifier",
            FT_STRING,
            BASE_NONE,
            NULL,
            0,
            NULL,
            HFILL }
        },
        { &hf_cannon_num, 
            { "Cannon Number",
            "cannon.num",
            FT_UINT8,
            BASE_DEC,
            NULL,
            0,
            NULL,
            HFILL }
        },
        { &hf_cannon_fire, 
            { "Cannon Fire",
            "cannon.fire",
            FT_UINT8,
            BASE_HEX,
            NULL,
            0x00,
            NULL,
            HFILL }
        },
        { &hf_cannon_fire_b[0], 
            { "Cannon Fire",
            "cannon.fire",
            FT_BOOLEAN,
            8,
            NULL,
            0x80,
            NULL,
            HFILL }
        },
        { &hf_cannon_fire_b[1], 
            { "Cannon Fire",
            "cannon.fire",
            FT_BOOLEAN,
            8,
            NULL,
            0x40,
            NULL,
            HFILL }
        },
        { &hf_cannon_fire_b[2], 
            { "Cannon Fire",
            "cannon.fire",
            FT_BOOLEAN,
            8,
            NULL,
            0x20,
            NULL,
            HFILL }
        },
        { &hf_cannon_fire_b[3], 
            { "Cannon Fire",
            "cannon.fire",
            FT_BOOLEAN,
            8,
            NULL,
            0x10,
            NULL,
            HFILL }
        },
        { &hf_cannon_fire_b[4], 
            { "Cannon Fire",
            "cannon.fire",
            FT_BOOLEAN,
            8,
            NULL,
            0x08,
            NULL,
            HFILL }
        },
        { &hf_cannon_fire_b[5], 
            { "Cannon Fire",
            "cannon.fire",
            FT_BOOLEAN,
            8,
            NULL,
            0x04,
            NULL,
            HFILL }
        },
        { &hf_cannon_fire_b[6], 
            { "Cannon Fire",
            "cannon.fire",
            FT_BOOLEAN,
            8,
            NULL,
            0x02,
            NULL,
            HFILL }
        },
        { &hf_cannon_fire_b[7], 
            { "Cannon Fire",
            "cannon.fire",
            FT_BOOLEAN,
            8,
            NULL,
            0x01,
            NULL,
            HFILL }
        }
    };

    static gint *ett[] = {
        &ett_cannonade
    };

    proto_cannonade = proto_register_protocol (
            "CANNONADE Protocol", /* name       */
            "Cannonade",          /* short name */
            "cannonade"           /* abbrev     */
            );

    proto_register_field_array(proto_cannonade, hf, array_length(hf));
    proto_register_subtree_array(ett, array_length(ett));
}

void proto_reg_handoff_cannonade(void)
{
    static dissector_handle_t cannonade_handle;

    cannonade_handle = \
        create_dissector_handle(dissect_cannonade, proto_cannonade);
    dissector_add_uint("udp.port", CANNONADE_PORT, cannonade_handle);
}

static void dissect_cannonade(tvbuff_t *tvb, 
        packet_info *pinfo, proto_tree *tree)
{
    int i;
    gint offset = 0;
    guint8 cannon_num = 0;

    col_set_str(pinfo->cinfo, COL_PROTOCOL, "CANNONADE");
    /* Clear out stuff in the info column */
    col_clear(pinfo->cinfo,COL_INFO);

    if (tree) {
        proto_item *ti = NULL;
        proto_tree *cannonade_tree = NULL;
        
        ti = proto_tree_add_item(tree, 
                proto_cannonade, tvb, 0, -1, ENC_NA);
        cannonade_tree = proto_item_add_subtree(ti, ett_cannonade);

        proto_tree_add_item(cannonade_tree, hf_cannonade_id, 
                tvb, offset, 9, ENC_BIG_ENDIAN);
        offset += 9;
        proto_tree_add_item(cannonade_tree, hf_cannon_num,
                tvb, offset, 1, ENC_BIG_ENDIAN);
        cannon_num = tvb_get_guint8(tvb, offset);
        for (i = 0; i < cannon_num; ++i)
        {
            if (i % 8 == 0)
                offset += 1;
            proto_tree_add_item(cannonade_tree, hf_cannon_fire_b[i % 8],
                    tvb, offset, 1, ENC_BIG_ENDIAN);
        }
    }
}
