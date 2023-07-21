import "./RewardsController_base.spec";

import "./OneAssetOneReward/claimEqual.spec";
import "./OneAssetOneReward/claimFull.spec";

use invariant user_index_LEQ_index;

use rule shouldClaimAgainAfterBlocks;
use rule user_index_keeps_growing;
use rule claimSome;

