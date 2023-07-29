import "./RewardsController_base.spec";
import "./methods/Methods_more.spec";
import "./OneAsset/oneAsset.spec";
import "./OneAssetOneReward/oneAssetOneReward.spec";
import "./OneAssetOneReward/oneReward.spec";
import "./OneAssetOneReward/oneClaim.spec";
import "./OneAssetOneReward/oneClaimSome.spec";
import "./OneAssetOneReward/oneClaimMore.spec";
import "./OneAssetOneReward/oneClaimEqual.spec";

use invariant user_index_LEQ_index;

use rule index_keeps_growing;
use rule noDoubleClaim;
use rule onlyAuthorizeCanDecrease;

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

