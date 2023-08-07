import "./RewardsController_base.spec";
import "./methods/Methods_more.spec";
import "./common/invariants.i.spec";
import "./common/math.d.spec";
import "./common/harness.d.spec";
import "./common/assets.f.spec";
import "./common/reverts.f.spec";
import "./common/rewards.f.spec";
import "./common/claim.r.spec";
import "./common/setup.r.spec";
import "./common/zeroAddress.r.spec";
import "./common/rewardsCalculate.f.spec";
import "./rewardsTwo/rewardsTwoClaim.r.spec";
import "./rewardsTwo/rewardsTwo.r.spec";

using DummyERC20_rewardTokenB as RewardB;

///////////// Properties with One Asset Multiple Rewards /////////////
use invariant user_index_LEQ_index;
use invariant timestamp;
use invariant rewardEnabled;

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
// use invariant rewardsLength;
// use rule rewardTwoUserRewards;

// FAILS
