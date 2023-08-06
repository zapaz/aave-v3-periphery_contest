import "./RewardsController_base.spec";
import "./methods/Methods_more.spec";
import "./common/invariants.i.spec";
import "./common/math.d.spec";
import "./common/harness.d.spec";
import "./common/claim.r.spec";
import "./common/assets.f.spec";
import "./common/reverts.f.spec";
import "./common/setup.r.spec";
import "./common/rewards.f.spec";
import "./common/rewardsCalculate.f.spec";
import "./common/zeroAddress.r.spec";
import "./rewardOne/rewardOneConfigureAsset.r.spec";
import "./rewardOne/rewardOne.r.spec";
import "./rewardOne/rewardOneClaim.r.spec";
import "./rewardOne/rewardOneClaimSome.r.spec";
import "./rewardOne/rewardOneClaimMonotonicity.r.spec";
import "./rewardOne/rewardOneUserRewards.r.spec";

using TransferStrategyHarness as TransferStrategy;


///////////// Properties with One Asset Multiple Rewards /////////////
use invariant user_index_LEQ_index;
use invariant timestamp;

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

///////////// Properties with One Asset One Reward /////////////
use rule rewardOneUserRewards;

use rule rewardOneByAssetIsInList;

use rule rewardOneClaimAllRewardsOnBehalfAsExpected;  // SLOW
use rule rewardOneClaimRewardsAsExpected;
use rule rewardOneClaimRewardsOnBehalfAsExpected;

use rule rewardOneClaimMonotonicityEmission;

use rule rewardOneClaimSome;

use rule rewardOneConfigureAsset;

// TIMEOUT
use rule rewardOneClaimAllRewardsToSelfAsExpected;
use rule rewardOneClaimAllRewardsAsExpected;
use rule rewardOneClaimMonotonicityTime;
use rule rewardOneClaimMonotonicityAssets;
use rule rewardOneClaimUserRewards;
use rule rewardOneClaimRewardsToSelfAsExpected;
use rule rewardOneClaimTwice;


// TESTING

// FAILS
