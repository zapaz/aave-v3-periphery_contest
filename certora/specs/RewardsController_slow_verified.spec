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
import "./common/zeroAddress.r.spec";
import "./rewardOne/rewardOneConfigureAsset.r.spec";
import "./rewardOne/rewardOne.r.spec";
import "./rewardOne/rewardOneClaim.r.spec";
import "./rewardOne/rewardOneClaimSome.r.spec";
import "./rewardOne/rewardOneClaimMonotonicity.r.spec";
import "./rewardOne/rewardOneUserRewards.r.spec";

// SLOW
use rule rewardOneClaimAllRewardsToSelfAsExpected;
use rule rewardOneClaimAllRewardsAsExpected;
use rule rewardOneClaimMonotonicityTime;
use rule rewardOneClaimMonotonicityAssets;
use rule rewardOneClaimUserRewards;
use rule rewardOneClaimRewardsToSelfAsExpected;
use rule rewardOneClaimTwice;
