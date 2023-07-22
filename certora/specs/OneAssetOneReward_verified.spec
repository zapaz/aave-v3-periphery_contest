import "RewardsController_base.spec";
import "methods/Methods_more.spec";

import "OneAssetOneReward/oneClaim.spec";

use invariant user_index_LEQ_index;

use rule oneClaimAllRewardsAsExpected;
use rule oneClaimAllRewardsToSelfAsExpected;
use rule oneClaimAllRewardsOnBehalfAsExpected;
use rule oneClaimRewardsAsExpected;
use rule oneClaimRewardsOnBehalfAsExpected;
use rule oneClaimRewardsToSelfAsExpected;

use rule oneClaimRewardUnchanged;


// import "./OneAssetOneReward/claimEqual.spec";
// import "./OneAssetOneReward/claimFull.spec";
//
// use rule shouldClaimAgainAfterBlocks;
// use rule user_index_keeps_growing;
// use rule claimSome;

