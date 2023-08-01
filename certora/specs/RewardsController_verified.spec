import "./RewardsController_base.spec";
import "./common/methods.m.spec";
import "./common/math.d.spec";
import "./common/assets.f.spec";
import "./common/reverts.f.spec";
import "./common/setup.r.spec";
import "./common/rewards.f.spec";
import "./common/rewards.i.spec";
import "./rewardOne/rewardOne.r.spec";
import "./rewardOne/rewardOneClaim.r.spec";
import "./rewardOne/rewardOneClaimSome.r.spec";
import "./rewardOne/rewardOneClaimMonotonicity.r.spec";
import "./rewardOne/rewardOneClaimEqual.r.spec";

using TransferStrategyHarness as TransferStrategy;

use invariant user_index_LEQ_index;
use invariant rewardsZero;

use rule index_keeps_growing;
use rule noDoubleClaim;
use rule onlyAuthorizeCanDecrease;

///////////////// Properties ///////////////////////

use rule revertsNotAllways;

use rule rewardOneByAssetIsInList;

use rule rewardOneClaimSome;
use rule rewardOneClaimRewardsAsExpected;


// SLOW
use rule rewardOneClaimRewardsOnBehalfAsExpected;
use rule rewardOneClaimRewardsToSelfAsExpected;

use rule rewardOneClaimUserRewards;
use rule rewardOneClaimAllRewardsAsExpected;

// use rule rewardOneClaimEqual;

use rule rewardOneClaimMonotonicityAssets;
use rule rewardOneClaimMonotonicityTime;

use rule setupConfig;