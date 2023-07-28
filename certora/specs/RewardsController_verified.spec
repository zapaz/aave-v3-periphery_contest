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

use rule oneClaimAllRewardsAsExpected;
use rule oneClaimAllRewardsToSelfAsExpected;
use rule oneClaimAllRewardsOnBehalfAsExpected;
use rule oneClaimRewardsAsExpected;
use rule oneClaimRewardsOnBehalfAsExpected;
use rule oneClaimRewardsToSelfAsExpected;

use rule oneClaimSome;

use rule oneClaimEqual;
use rule oneClaimEqualUserRewards;

use rule oneClaimMoreAssets;
// use rule oneClaimMoreTime;
// use rule oneClaimLessTotalSupply;

