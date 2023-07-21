import "./RewardsController_base.spec";

use invariant user_index_LEQ_index;

use rule index_keeps_growing;
use rule noDoubleClaim;
use rule onlyAuthorizeCanDecrease;

