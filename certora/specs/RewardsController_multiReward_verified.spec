import "./RewardsController_base.spec";
import "./common/methods.m.spec";
import "./common/math.d.spec";
import "./common/harness.d.spec";
import "./common/assets.f.spec";
import "./common/reverts.f.spec";
import "./common/rewards.f.spec";
import "./common/claim.r.spec";
import "./common/setup.r.spec";
import "./common/zeroAddress.r.spec";
import "./rewardsMulti/rewardsMultiClaim.r.spec";
import "./rewardsMulti/rewardsMulti.r.spec";

using DummyERC20_rewardTokenB as RewardB;

use invariant indexIncreaseWithSomeAvailableReward;
use invariant userIndexIncreaseWithSomeAvailableReward;

// COMMON (IN MULTI AND ONE)
use invariant user_index_LEQ_index;

use rule index_keeps_growing;
use rule noDoubleClaim;
use rule onlyAuthorizeCanDecrease;

use rule revertsNotAllways;

use rule setupAssetsAdded;
use rule setupRewardModified;
use rule setupTransferStrategy;
use rule setupRewardOracle;
use rule setupClaimer;

use rule claimRewardsReverts;
use rule claimRewardsOnBehalfReverts;
use rule claimAllRewardsReverts;
use rule claimAllRewardsOnBehalfReverts;

/// testing
use rule availableRewardsCountIncrease;

///////////////// Properties ///////////////////////

use rule rewardsMultiByAssetAreInList;

use rule zeroAddressAssetUnchanged;
use rule zeroAddressRewardUnchanged;
use rule zeroAddressStrategyCannotBeSet;

// SLOW

use rule rewardsMultiClaimAllRewardsAsExpected;
use rule rewardsMultiClaimAllRewardsToSelfAsExpected;
use rule rewardsMultiClaimAllRewardsOnBehalfAsExpected;

use rule rewardsMultiClaimRewardsAsExpected;
use rule rewardsMultiClaimRewardsOnBehalfAsExpected;
use rule rewardsMultiClaimRewardsToSelfAsExpected;
use rule rewardsMultiClaimUserRewards;