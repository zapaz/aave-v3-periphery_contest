import "./methods/Methods_base.spec";
import "./methods/Methods_more.spec";
import "./OneAsset/oneAsset.spec";
import "./OneAssetMultiRewards/zero.spec";
import "./OneAssetMultiRewards/multiClaim.spec";
import "./OneAssetMultiRewards/multiRewards.spec";
import "./OneAssetMultiRewards/oneAssetMultiRewards.spec";

using DummyERC20_rewardTokenB as RewardB;

///////////////// Properties ///////////////////////

use rule multiClaimAllRewardsAsExpected;
use rule multiClaimAllRewardsToSelfAsExpected;
use rule multiClaimAllRewardsOnBehalfAsExpected;

// use rule multiClaimRewardsAsExpected;
// use rule multiClaimRewardsOnBehalfAsExpected;
// use rule multiClaimRewardsToSelfAsExpected;
// use rule multiClaimUserRewards;