import "./RewardsController_base.spec";
import "./methods/Methods_more.spec";
import "./OneAsset/oneAsset.spec";
import "./OneAssetOneReward/oneAssetOneReward.spec";
import "./OneAssetOneReward/oneClaim.spec";
// import "./OneAssetOneReward/claimEqual.spec";
// import "./OneAssetOneReward/claimFull.spec";
import "./OneAssetOneReward/oneReward.spec";


using DummyERC20_rewardTokenB as RewardB;

// use invariant rewardByAssetIsInList;

// use invariant user_index_LEQ_index;

// use rule index_keeps_growing;
// use rule noDoubleClaim;
// use rule onlyAuthorizeCanDecrease;

use rule oneClaimAllRewardsAsExpected;
use rule oneClaimAllRewardsToSelfAsExpected;
use rule oneClaimAllRewardsOnBehalfAsExpected;
use rule oneClaimRewardsAsExpected;
use rule oneClaimRewardsOnBehalfAsExpected;
use rule oneClaimRewardsToSelfAsExpected;

// use rule zeroAddressAssetUnchanged;
// use rule zeroAddressRewardUnchanged;
// use rule cannotSetTransferStrategyToZero;

