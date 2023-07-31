import "./RewardsController_base.r.spec";
import "./methods/Methods_more.m.spec";
import "./common/math.f.spec";
import "./common/oneAsset.f.spec";
import "./common/reverts.f.spec";
import "./oneReward/oneReward.f.spec";
import "./oneReward/oneReward.r.spec";
import "./oneReward/oneClaim.r.spec";
import "./oneReward/oneClaimSome.r.spec";
import "./oneReward/oneClaimMore.r.spec";
import "./oneReward/oneClaimEqual.r.spec";

use invariant user_index_LEQ_index;

use rule index_keeps_growing;
use rule noDoubleClaim;
use rule onlyAuthorizeCanDecrease;

///////////////// Properties ///////////////////////

use rule revertsNotAllways;

use rule oneRewardByAssetIsInList;

use rule oneClaimRewardsAsExpected;


// SLOW
use rule oneClaimRewardsOnBehalfAsExpected;
use rule oneClaimRewardsToSelfAsExpected;

use rule oneClaimUserRewards;
use rule oneClaimAllRewardsAsExpected;

use rule oneClaimSome;
// use rule oneClaimEqual;

use rule oneClaimMoreAssets;
// use rule oneClaimMoreTime;
// use rule oneClaimLessTotalSupply;

