import "./RewardsController_base.spec";
import "./common/methods.m.spec";
import "./common/math.d.spec";
import "./common/harness.d.spec";
import "./common/claim.r.spec";
import "./common/assets.f.spec";
import "./common/reverts.f.spec";
import "./common/setup.r.spec";
import "./common/rewards.f.spec";
import "./rewardOne/rewardOneSetup.r.spec";
import "./rewardOne/rewardOne.r.spec";
import "./rewardOne/rewardOneClaim.r.spec";
import "./rewardOne/rewardOneClaimSome.r.spec";
import "./rewardOne/rewardOneClaimMonotonicity.r.spec";
import "./rewardOne/rewardOneClaimEqual.r.spec";

using TransferStrategyHarness as TransferStrategy;

use invariant userIndexIncreaseWithSomeAvailableReward;

// COMMON (IN MULTI AND ONE)
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

// ///////////////// Properties ///////////////////////

use rule setupConfig;
use rule rewardOneByAssetIsInList;

use rule rewardOneClaim;
use rule rewardOneClaimAllRewardsAsExpected;
use rule rewardOneClaimAllRewardsOnBehalfAsExpected;
use rule rewardOneClaimRewardsAsExpected;
use rule rewardOneClaimRewardsOnBehalfAsExpected;
use rule rewardOneClaimRewardsToSelfAsExpected;

use rule rewardOneClaimSome;
use rule rewardOneClaimMonotonicityTime;


// SLOW
use rule rewardOneClaimUserRewards;
use rule rewardOneClaimAllRewardsToSelfAsExpected;
use rule rewardOneClaimMonotonicityAssets;

// FAILS
use rule rewardOneClaimEqual;
