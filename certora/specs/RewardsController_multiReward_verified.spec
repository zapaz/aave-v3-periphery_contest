import "./RewardsController_base.spec";
import "./common/methods.m.spec";
import "./common/math.d.spec";
import "./common/harness.d.spec";
import "./common/assets.f.spec";
import "./common/reverts.f.spec";
import "./common/rewards.f.spec";
import "./common/setup.r.spec";
import "./common/zeroAddress.r.spec";
import "./rewardsMulti/rewardsMultiClaim.r.spec";
import "./rewardsMulti/rewardsMulti.r.spec";

using DummyERC20_rewardTokenB as RewardB;

use invariant user_index_LEQ_index;

use rule index_keeps_growing;
use rule noDoubleClaim;
use rule onlyAuthorizeCanDecrease;

///////////////// Properties ///////////////////////

use rule revertsNotAllways;

use rule rewardsMultiByAssetAreInList;

use rule zeroAddressAssetUnchanged;
use rule zeroAddressRewardUnchanged;
use rule zeroAddressStrategyCannotBeSet;

// SLOW

use rule rewardsMultiClaimAllRewardsAsExpected;
use rule rewardsMultiClaimAllRewardsToSelfAsExpected;
use rule rewardsMultiClaimAllRewardsOnBehalfAsExpected;

use rule setupAssetsAdded;
use rule setupRewardModified;
use rule setupTransferStrategy;
use rule setupRewardOracle;

// use rule rewardsMultiClaimRewardsAsExpected;
// use rule rewardsMultiClaimRewardsOnBehalfAsExpected;
// use rule rewardsMultiClaimRewardsToSelfAsExpected;
// use rule rewardsMultiClaimUserRewards;