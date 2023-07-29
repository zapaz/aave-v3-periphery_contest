import "./RewardsController_base.spec";
import "./methods/Methods_more.spec";
import "./OneAsset/oneAsset.spec";
import "./OneAssetOneReward/oneAssetOneReward.spec";
import "./OneAssetOneReward/oneReward.spec";
import "./OneAssetOneReward/oneClaim.spec";
import "./OneAssetOneReward/oneClaimSome.spec";
import "./OneAssetOneReward/oneClaimMore.spec";
import "./OneAssetOneReward/oneClaimEqual.spec";

use rule oneClaimUserRewards;
use rule oneClaimRewardsToSelfAsExpected;
use rule oneClaimRewardsOnBehalfAsExpected;
use rule oneClaimAllRewardsAsExpected;

use rule oneClaimSome;
// use rule oneClaimEqual;

use rule oneClaimMoreAssets;
// use rule oneClaimMoreTime;
// use rule oneClaimLessTotalSupply;

