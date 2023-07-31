import "./RewardsController_base.r.spec";

using DummyERC20_rewardTokenB as RewardB;

use invariant user_index_LEQ_index;

use rule index_keeps_growing;
use rule noDoubleClaim;
use rule onlyAuthorizeCanDecrease;

