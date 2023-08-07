rule revertsNotAllways(method f, env e, calldataarg arg){
    f(e, arg);

    satisfy true;
}
