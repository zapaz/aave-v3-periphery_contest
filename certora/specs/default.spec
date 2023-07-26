import "methods/Methods_base.spec";
import "methods/Methods_more.spec";
import "RewardsController_base.spec";

import "OneAssetMultiRewards/zero.spec";
import "OneAssetMultiRewards/invariant.spec";
import "OneAssetOneReward/oneClaim.spec";
// import "./OneAssetOneReward/claimEqual.spec";
// import "./OneAssetOneReward/claimFull.spec";

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

// use rule shouldClaimAgainAfterBlocks;
// use rule user_index_keeps_growing;
// use rule claimSome;

// use rule zeroAddressAssetUnchanged;
// use rule zeroAddressRewardUnchanged;
// use rule cannotSetTransferStrategyToZero;

