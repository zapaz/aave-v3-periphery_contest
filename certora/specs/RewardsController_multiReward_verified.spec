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
import "./rewardsTwo/rewardsTwoClaim.r.spec";
import "./rewardsTwo/rewardsTwo.r.spec";

using DummyERC20_rewardTokenB as RewardB;

///////////// Properties with One Asset Multiple Rewards /////////////
use invariant user_index_LEQ_index;

use rule index_keeps_growing;
use rule noDoubleClaim;
use rule onlyAuthorizeCanDecrease;

use rule revertsNotAllways;

use rule setupAssetImmutable;
use rule setupAssetsAdded;
use rule setupRewardModified;
use rule setupTransferStrategy;
use rule setupRewardOracle;
use rule setupClaimer;

use rule claimRewardsReverts;
use rule claimRewardsOnBehalfReverts;
use rule claimAllRewardsReverts;
use rule claimAllRewardsOnBehalfReverts;

use rule zeroAddressAssetUnchanged;
use rule zeroAddressRewardUnchanged;
use rule zeroAddressStrategyCannotBeSet;

///////////// Properties with One Asset Two Rewards /////////////
use rule rewardsTwoByAssetAreInList;

use rule availableRewardsCountProperties;

// TIMEOUT
// use rule rewardsTwoClaimAllRewardsAsExpected;
// use rule rewardsTwoClaimAllRewardsToSelfAsExpected;
// use rule rewardsTwoClaimAllRewardsOnBehalfAsExpected;
// use rule rewardsTwoClaimRewardsAsExpected;
// use rule rewardsTwoClaimRewardsOnBehalfAsExpected;
// use rule rewardsTwoClaimRewardsToSelfAsExpected;
// use rule rewardsTwoClaimUserRewards;

// TESTING

// FAILS
