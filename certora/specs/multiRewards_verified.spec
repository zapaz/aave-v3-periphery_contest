import "./RewardsController_base.r.spec";
import "./methods/Methods_more.m.spec";
import "./common/math.f.spec";
import "./common/oneAsset.f.spec";
import "./common/reverts.f.spec";
import "./common/setup.r.spec";
import "./common/zeroAddress.r.spec";
import "./multiRewards/multiRewards.f.spec";
import "./multiRewards/multiClaim.r.spec";
import "./multiRewards/multiRewards.r.spec";

using DummyERC20_rewardTokenB as RewardB;

use invariant user_index_LEQ_index;

use rule index_keeps_growing;
use rule noDoubleClaim;
use rule onlyAuthorizeCanDecrease;

///////////////// Properties ///////////////////////

use rule revertsNotAllways;

use rule rewardsByAssetAreInList;

use rule zeroAddressAssetUnchanged;
use rule zeroAddressRewardUnchanged;
use rule zeroAddressStrategyCannotBeSet;

// SLOW

use rule multiClaimAllRewardsAsExpected;
use rule multiClaimAllRewardsToSelfAsExpected;
use rule multiClaimAllRewardsOnBehalfAsExpected;

use rule setupAssetsAdded;
use rule setupRewardModified;
use rule setupTransferStrategy;
use rule setupRewardOracle;

// use rule multiClaimRewardsAsExpected;
// use rule multiClaimRewardsOnBehalfAsExpected;
// use rule multiClaimRewardsToSelfAsExpected;
// use rule multiClaimUserRewards;